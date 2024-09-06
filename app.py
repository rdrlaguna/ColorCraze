from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify # type: ignore
from flask_session import Session
from random import randint
from werkzeug.security import check_password_hash, generate_password_hash # type: ignore

from helpers import (
    login_required, showError, from_hex_to_rgb, from_rgb_to_hsl, validateHex, 
    get_time, valid_color, color_has_votes, validate_username, validate_password,
    color_picker_value)

# Configure Flask application
app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///colors.db")

# Set order options for the color list
OPTIONS = [
    "Name",
    "Hue",
    "Saturation",
    "Light",
    "Most recent",
]


# Render index.html
@app.route("/")
def index():
    """Show main page"""

    return render_template("index.html")
 

# Renders topColors.html
@app.route("/top")
def top():
    """Show all top colors voted by users"""

    # Query data from db asking for top voted colors
    topColors = db.execute(
        "SELECT color_name, " +
                "hex, " +
                "light, " +
                "voted_colors.votes, " +
                "username " +
        "FROM colors " +
        "JOIN voted_colors ON colors.id = voted_colors.color_id " +
        "JOIN users ON colors.user_id = users.id " +
        "ORDER BY (voted_colors.votes) DESC LIMIT 3"
    )

    return render_template("topColors.html", topColors=topColors)


# Renders vote.html
@app.route("/vote", methods=["GET", "POST"])
def vote():
    """Show a form to let users vote"""

    if request.method == "POST":
        # Get the voted color
        color = request.form.get("color").strip().title()

        # Validate user's left votes
        userVotes = db.execute(
            "SELECT votes FROM users WHERE id = ?", session["user_id"]
        )

        if userVotes[0]["votes"] <= 0:
            flash("You don't have enough votes left!", "error")
            return redirect("/vote")

        # Validate color name
        colorList = db.execute (
            "SELECT color_name FROM colors"
        )

        if not color:
            return showError("Introduce a color!", "vote", 400)
        
        if not valid_color(colorList, color):
            return showError("Select a valid color!", "vote", 400)
        

        # Update user's number of votes
        votesLeft = userVotes[0]["votes"] - 1
        db.execute(
            "UPDATE users SET votes = ? WHERE id = ?", votesLeft, session["user_id"]
        )

        # Add a vote for the selected color
        # Find if the color already has votes from that user
        colorId = db.execute(
            "SELECT id FROM colors WHERE color_name = ?", color
        ) 
        # Gets the user's votes
        votedColors = db.execute(
            "SELECT * FROM voted_colors WHERE user_id = ?", session["user_id"]
        )

        date = get_time()

        # UPDATE if user has already voted that color
        if color_has_votes(votedColors, colorId[0]["id"]):
            totalVotes = db.execute(
                "SELECT votes FROM voted_colors WHERE user_id = ? AND color_id = ?", session["user_id"], colorId[0]["id"]
            )
            
            newVotes = totalVotes[0]["votes"] + 1
            db.execute (
                "UPDATE voted_colors SET votes = ?, date = ?, hour = ? " +
                "WHERE user_id = ? AND color_id = ?", 
                newVotes, date["date"], date["hour"], session["user_id"], colorId[0]["id"] 
            )
            
        # INSERT if user didn't vote for that color
        else:
            votes = 1
            db.execute(
                "INSERT INTO voted_colors (" +
                    "user_id, color_id, " + 
                    "votes, date, hour) " +
                "VALUES (" +
                    "?, ?, ?, ?, ?)",
                session["user_id"], colorId[0]["id"], votes, date["date"], date["hour"]
            )   
        
        flash("You have submitted your vote.")
        return redirect("/vote")
    
    else:
        # Select colors for display
        colors = db.execute (
            "SELECT hex, color_name FROM colors"
        )
       
        return render_template("vote.html", colors=colors)


@app.route("/search")
def search():
    """ Enable autocomplete when looking for a color to vote """

     # Enable autocomplete
    q = request.args.get("q")
    if q:
        colors = db.execute(
            "SELECT color_name, hex FROM colors WHERE color_name Like ? Limit 50", "%" + q + "%"
        )
    else:
        colors =[]

    return jsonify(colors)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # Get user's input
        name = request.form.get("name").strip().lower()
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        print(password)

        # Validate username
        if name == "" :
            return showError("Introduce a user name", 400)
        elif validate_username(name) == False :
            return showError("Introduce a valid username", "register", 400)
        
        # Validate password
        if (password == "" or
            password != confirmation or
            validate_password(password, name) == False):
            return showError("Introduce a valid password", "register", 400)
        else:
            hash = generate_password_hash(password)

        # Register User in the database
        # Get registration date
        registered = get_time()

        # Return Error if the username already exists
        try: 
            db.execute("INSERT INTO users(username, hash, date) VALUES (?, ?, ?)",
                       name, hash, registered["date"])
        except ValueError:
            return showError("The user already exists", 400)
        
        # Confirm registration
        flash("You are now registered. Please, log in!")
        return redirect("/")
    
    # User reached route via GET (clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log user in """

    # Forget any user id
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Check if username was submitted
        if not request.form.get("name"):
            return showError("Provide a valid username", 400)
        # Check if password was submitted
        elif not request.form.get("password"):
            return showError("Please enter a password", 400)
        
        # Query the database for the username information
        userInfo = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("name")
        )

        # Ensure the username exists 
        if len(userInfo) != 1:
            return showError("Invalid user name", 400)
        # Check if it's a valid password
        elif not check_password_hash(userInfo[0]["hash"], request.form.get("password")):
            return showError("Invalid password", 400)

        # Remember which user has logged in
        session["user_id"] = userInfo[0]["id"]

        # Redirect user to home page
        return redirect("/")
    
    # User reached route via GET
    else: 
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user id
    session.clear()

    # Redirect user to home page
    return redirect("/")


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """Allow user to change password"""

    if request.method == "POST":

        oldPassword = request.form.get("oldPass")
        newPassword = request.form.get("newPass")
        confirmation = request.form.get("confirmation")
        
        # Validate old password
        # Get old password hash
        userHash = db.execute(
            "SELECT hash FROM users WHERE id = ?", session["user_id"]
        )

        oldHash = userHash[0]["hash"]
        if check_password_hash(oldHash, oldPassword) == False:
            return showError("Introduce your old password", 400)

        # Validate new password
        if (newPassword == "" or 
           newPassword != confirmation or
           newPassword == oldPassword):
            return showError("Invalid password", 400)
        
        # Generate new password hash
        newHash = generate_password_hash(newPassword)

        # Update new hash in database
        db.execute(
            "UPDATE users SET hash = ? WHERE id = ?", newHash, session["user_id"]
        )

        flash("You changed your password")
        return redirect("/account")

    else:
        userInfo = db.execute(
            "SELECT username, date, votes FROM users WHERE id = ?", session["user_id"]
        )
        name = userInfo[0]["username"].title()
        return render_template("account.html", name=name, userInfo=userInfo)


@app.route("/changeName", methods=["POST"])
@login_required
def changeName():
    """ Allow users to change username """

    # Get new name
    new_name = request.form.get('newName').strip().lower()

    # Validate new name
    if (new_name == "" or 
        validate_username(new_name) == False) :
        # Get userInfo
        userInfo = db.execute(
            "SELECT username, date, votes FROM users WHERE id = ?", session["user_id"]
        )
        name = userInfo[0]["username"].title()

        flash("Introduce a valid username", "error")
        return render_template("account.html", name=name, userInfo=userInfo)
    

    # Update new name
    db.execute (
        "UPDATE users SET username = ? WHERE id = ?", new_name, session["user_id"] 
    )

    # Retrieve updated userdata
    userInfo = db.execute(
            "SELECT username, date, votes FROM users WHERE id = ?", session["user_id"]
        )
    name = userInfo[0]["username"].title()

    # Render Account page
    return render_template("account.html", name=name, userInfo=userInfo)


# Renders colorList.html
@app.route("/addColor", methods=["GET", "POST"])
def addColor():
    """Allow user to add a new color to the database"""

    if request.method == "POST":

        # Get user hex color
        colorName = request.form.get("colorName").strip().title()
        colorHex = request.form.get("colorHex")

        # Validate if both fields contain data
        if colorName == "" or colorHex == "":
            return showError("Please, fill every field.", "addColor", 400)
        
        if not validateHex(colorHex):
            return showError("Please enter a valid hexadecimal number.", "addColor", 400)
        

        # Validate name constrains
        # colorName.count(" ") > 1 or
        if (len(colorName) > 20 or 
            colorName.count(" ") > 1 or
            colorName.replace(" ", "").isalpha() == False):
            return showError("Oops! Color Naming Rules Alert!", "colorName", 400)

        # Turn color to RGB
        colorRGB = from_hex_to_rgb(colorHex)

        # Turn color to HSL
        colorHSL = from_rgb_to_hsl(colorRGB)

        # Get submission date 
        date = get_time()

        # Insert color in DB
        try:
            db.execute(
                "INSERT INTO colors (" +
                    "user_id, color_name, " +
                    "hex, red, green, blue, " +
                    "hue, saturation, light, " +
                    "date, hour) "+
                "VALUES (?, ?, ?, " +
                        "?, ?, ?, ?, " +
                        "?, ?, ?, ?)",
                session["user_id"], colorName, colorHex, 
                colorRGB[0], colorRGB[1], colorRGB[2], colorHSL[0], 
                colorHSL[1], colorHSL[2], date["date"], date["hour"]
            )
        except ValueError:
            print(ValueError)
            return showError("The color already exists", 200)
        
        # Update user's votes
        current_votes = db.execute (
            "SELECT votes FROM users WHERE id = ?", session["user_id"] 
        )

        new_votes = current_votes[0]["votes"] + 3

        # Insert votes
        db.execute (
            "UPDATE users SET votes = ? WHERE id = ?", new_votes, session["user_id"]
        )
        
        flash("You added a new color to the list!")
        return redirect("/addColor")
    
    else:

        # Query for all colors on the database
        colors = db.execute(
            "SELECT color_name, light, hex FROM colors"
        )

        # Get a random Color Picker value
        color_value = color_picker_value(colors)

        return render_template("colorList.html", colors=colors, 
                               options=OPTIONS, color_value=color_value)


@app.route("/orderColor", methods=["GET", "POST"])
def orderColor():
    """Order the color list with the selected criteria"""

    if request.method == "POST":

        order = request.form.get("order")

        # Validate if order is correct
        if not order or order not in OPTIONS:
                return showError("Plese, select a valid option", 400)

        # Query database for colors
        # Order by NAME
        if order == OPTIONS[0]:
            colors = db.execute(
                "SELECT color_name, hex, light FROM colors ORDER BY color_name ASC"
            )
        # Order by HUE
        elif order ==  OPTIONS[1]:
            colors = db.execute(
                "SELECT color_name, hex, hue, light FROM colors ORDER BY hue DESC"
            )
        # Order by SATURATION
        elif order ==  OPTIONS[2]:
            colors = db.execute(
                "SELECT color_name, hex, saturation, light FROM colors ORDER BY saturation DESC"
            )
        # Order by LIGHT
        elif order ==  OPTIONS[3]:
            colors = db.execute(
                "SELECT color_name, hex, light FROM colors ORDER BY light DESC"
            )
        # Order by recent
        elif order ==  OPTIONS[4]:
            colors = db.execute(
                "SELECT color_name, hex, light FROM colors ORDER BY date DESC, hour DESC"
            )
        else :
            return showError("That criteria is not allowed", 400)

        # TODO: return color-picker value
        color_value = color_picker_value(colors)

        return render_template("colorList.html", colors=colors,
                               options=OPTIONS, color_value=color_value)
    
    else:
        return render_template("colorList.html")


@app.route("/colorDetails", methods=["POST"])
def colorDetails():
    """Shows the specific attributes for each color"""

    data = request.json
    colorHex = data.get("hex")

    # Get the color's information
    color = db.execute(
        "SELECT * FROM colors WHERE hex = ?", colorHex
    )

    # Get the user name
    user = db.execute (
        "SELECT username FROM users WHERE id = ?", color[0]["user_id"]
    )

    # Return the data in JSON format
    return jsonify({
        "message": "Data received",
        "user_id": color[0]["user_id"],
        "username": user[0]["username"],
        "name": color[0]["color_name"],
        "red": color[0]["red"],
        "green": color[0]["green"],
        "blue": color[0]["blue"],
        "hue": color[0]["hue"],
        "saturation": color[0]["saturation"],
        "light": color[0]["light"],
        "date": color[0]["date"]
    })


@app.route("/working")
def working():

    return showError("Sorry, this section is under construction.", "home", 400)


# ******************************************************************************
# T O    D O    L I S T :

    # Add date timestampt to user registration
    # Add Username and Password restrictions