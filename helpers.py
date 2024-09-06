import datetime
import pytz
from flask import redirect, render_template, request, session
from functools import wraps
from random import randint


def login_required(f):
    """Decorate routes to require login"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
        
    return decorated_function


def showError(message, type=None, code=400):
    """Render a message after an error"""

    return render_template("error.html", message=message, type=type, code=code)



def validate_username(name):
    """ Validate username upon registration """
    
    # Turn username to lowercase
    name = name.lower()

    # Check length between 3 to 15 characters
    if (len(name) < 3 or len(name) > 15):
        return False
    
    # Allow only letters, dots and undescores
    for i in range(len(name)):
        if name[i] == "." or name[i] == "_" :
            # Don't allow consecutive special characters
            if (i == len(name) - 1):
                continue
            elif name[ i+ 1] == "." or name[i + 1] == "_" :
                return False
            else:
                continue
        # Allow letters    
        elif name[i].isalpha():
            continue
        # Don't allow more than one word
        elif name[i] == " ":
            return False
        else:
            return False
        
    # List words that are not accepted as username
    reserved_words = [
        "admin", "administrator", "root", "sysadmin", "system",
        "guest", "test", "null", "undefined", "unknown", "user",
        "owner", "operator", "support", "superuser", "staff", 
        "moderator", "help", "default", "info", "email", "bot",
        "dev", "developer", "backend", "frontend", "master", "main",
        "service", "server", "localhost", "api", "database", "db",
        "data", "status", "supervisor", "controller", "manager", 
        "login", "logout", "register", "signup", "signin", "auth",
        "authenticator", "password", "profile", "account", "select",
        "insert", "delete", "update", "where", "join", "from", "table",
        "index", "group", "order", "by", "having", "primary", "foreign",
        "key"
        ]
    
    # Don't allow names inside the reserved words list
    if name in reserved_words :
        return False

    # Validate name
    return True    


def validate_password(password, username):
    """ Validate submited password upon registration """

    # Validate length
    passLen = len(password)
    if (passLen < 8 or passLen > 16):
        return False
    
    # Don't allow spaces or username in password
    if (" " in password or
        username in password):
        return False
    
    # Ensure character variety
    letterType = {
        'upper' : 0,
        'lower' : 0,
        'number' : 0,
        'special' : 0,
    }

    for letter in password:
        # Check for uppercase letters
        if letter.isupper() == True:
            letterType["upper"] += 1
        # Check for lowercase letters
        elif letter.islower() == True:
            letterType["lower"] += 1
        # Check for numbers
        elif letter.isnumeric() == True:
            letterType["number"] += 1
        # Check for special characters
        elif letter in ["!", "@", "#", "$", "%", "&"]:
            letterType["special"] += 1
        else:
            return False
        
    # Check for at least 1 character of each type 
    for key in letterType:
        if letterType[key] < 1:
            return False

    return True


def validateHex(hex_color):
    """ Validate submited hexadecimal code """

    if (hex_color[0] == "#") and (len(hex_color) == 7):
        return True
    else:
        return False

def from_hex_to_rgb(hex_color):
    """Convert an hexadecimal value to a RGB value"""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def from_rgb_to_hsl(rgb_color):
    """Convert RGB to HSL.
    Returns a tuple containing HSL values.
    """
    r = rgb_color[0] / 255.0
    g = rgb_color[1] / 255.0
    b = rgb_color[2] / 255.0

    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min

    # Calculate Lightness
    l = (c_max + c_min) / 2

    # Calculate Saturation
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

    # Calculate Hue
    if delta == 0:
        h = 0
    elif c_max == r:
        h = ((g - b) / delta) % 6
    elif c_max == g:
        h = (b - r) / delta + 2
    elif c_max == b:
        h = (r - g) / delta + 4

    h = round(h * 60)
    if h < 0:
        h += 360

    # Convert to percentage
    s = round(s * 100)
    l = round(l * 100)

    return (h, s, l)
    

def get_time():
    time = datetime.datetime.now(pytz.timezone("Europe/Madrid"))
    lsTime = str(time).split()
    date = lsTime[0]

    lsHour = lsTime[1].split(".")
    hour = lsHour[0]

    return {"date": date, "hour": hour}


# Validates if a color is inside a list of dictionaries
def valid_color(colorList, color):
    
    for i in range(len(colorList)):
        if color == colorList[i]["color_name"]:
            return True
        
    return False

# Check if a user has already voted for a color
def color_has_votes(votes, color_id):

    for i in range(len(votes)):
        if color_id == votes[i]["color_id"]:
            return True
        
    return False

def color_picker_value(colors):
    """ Returns a random value for the color picker """ 

    # Check if returns an empty list
    if not colors:
    # Give a default color-picker value
        color_value = '#A6A6A6'
    else:
        # Select random color as Color Picker val
        color_index = randint(0, len(colors) - 1)
        color_value = colors[color_index]["hex"]

    return color_value