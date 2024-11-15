# ColorCraze
Web app to list and vote for all your favorite colors.

#### Visit the web:  <https://rodrigolaguna.pythonanywhere.com/>

## Description

Welcome to **ColorCraze**, an interactive web application that allows users to explore, submit, and vote on a variety of custom colors. The app serves as a vibrant community for color enthusiasts to submit unique color hues, give them creative names, and cast votes to create a dynamic ranking of the most popular colors. Whether you're a designer looking for inspiration or just a lover of color, ColorCraze offers an engaging and playful way to interact with the world of color.

This project was developed as the final assignment for **cs50x: Introduction to Computer Science**. The primary goal of the project was to demonstrate the acquired knowledge of modern web technologies like **Python**, **Flask**, **HTML**, **CSS**, **JavaScript**, and **SQL**. The application features *user authentication*, *submission validation*, *dynamic ranking*, and *error handling*, making it a comprehensive project that showcases full-stack development skills.

## Table of Contents
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage and Features](#usage-and-features)
- [Design Decisions](#design-decisions)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

---

## Getting Started

To try out this project, follow these steps:

### 1. Prerequisites

Ensure you have a basic setup with the following:
- **A code editor** like [Visual Studio Code](https://code.visualstudio.com/) or Sublime Text.
- **Python 3.8+**
- **Flask**
- **SQLite** (optional, or replace with your preferred DBMS)

### 2. Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/rdrlaguna/ColorCraze.git
    cd project-name
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate 

    # On Windows use `env\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the Flask server:
    ```bash
    flask run
    ```

5. Access the web app at `http://127.0.0.1:5000/`.


## Project Structure

The repository is organized as follows.

``` bash
ColorCraze/
├── static/          
│   ├── script.js
│   └── styles.css 
├── templates/        
│   ├── account.html  
│   ├── colorList.html   
│   ├── error.html   
│   ├── index.html   
│   ├── layout.html   
│   ├── login.html   
│   ├── register.html   
│   ├── topColors.html     
│   └── vote.html      
├── app.py         
├── colors.db           
├── helpers.py            
├── README.md
└── requirements.txt
```
---

The project is structured into various files and folders, each with specific functionality that contributes to the overall application. Below is a breakdown of the files:

#### 1. `app.py`
This is the main Flask application file that runs the server. It contains all the routes for the app and manages HTTP requests (GET and POST) for the core functionality of the application. Here's an overview of the key routes:

- **`/` (home):** Displays the homepage with a list of the different features the site offers to their users. This page welcomes the users and guides them through the site. It renders the main page with the appropriate styling.
- **`account`:** Displays user's personal information (e.g., username, registration date, votes left). It also allows the user to change their password.
- **`/addColor`:** Allows logged-in users to submit a new color. This route checks the validity of the color name and hex code before adding the new color to the database. It displays a flashed alert message on top of the page when the submission is succesful. If the input provided by the user is not valid, redirects the user to the error page showing an explanatory message.
- **`changeName`:** Allows users to change their username, fulfilling all the name validation requirements.
- **`colorDetails`:** Shows specific attributes of each color (e.g., color name, hex code, rgb  values, hsl values). When the user clicks on a color of the list, a request is sent to the server, which returns that specific color's information using JSON format.
- **`/login`:** Handles user authentication (login) functionality. Upon successful login, users gain access to color submission and voting features. Redirects the user to the error page when they introduce invalid credentials.
- **`/logout`:** Clears the user information for the session, susccesfully login the user out. Redirects the user to the homepage.
- **`orderColor`:** Queries the database to order the color list with the selected criteria from a list of limited options.
- **`/register`:** Manages user registration. Usernames and passwords are validated before being stored securely in the database. Redirects the user to the error page when they introduce invalid credentials.
- **`/search`:**  Enables autocomplete when users introduce color's name to vote for.
- **`/top`:** Displays the three most voted colors sorted in descending oreder. Shows the color's name and the amount of recived votes.
- **`/vote`:** Allows users to vote on colors. Each vote is recorded and used to update the ranking of the colors in real-time.

#### 2. `static/` (Folder)
Contains all static files, including CSS and JavaScript.

- **`styles.css`:** This is the main stylesheet for the application, responsible for the overall look and feel. It defines responsive design rules to ensure the app looks great on both mobile and desktop.
- **`script.js`:** This JavaScript file handles any client-side logic. It may include event listeners for user interactions, such as submitting forms or clicking buttons. It also handles the styling of the ranking system and queries data from the server to display the individual information of each color of the list using a CSS modal container.

#### 3. `templates/` (Folder)
Contains all HTML templates used by Flask to render different pages. Here's an overview of the main templates:

- **`account.html`:** Provides the user the ability to consult and modify their personal information. It displays the username, the date of their registration and the number of votes they have left. It also allows users to change their password and username. 
- **`colorList.html`:** The template for the color submission page. It includes the form where users enter a color name and hex value.It also displays the list of colors along with their names and hex codes, providing the option to the user to sort the color list based on various criteria, enabling sorting by hue, saturation, brightness, or other color properties to help users discover new favorites in their desired color range.
- **`error.html`:** The error page template that provides feedback to users when they violate input rules or encounter issues with the application. This page is rendered by a function that provides a custom error message tailored to each specific error.
- **`index.html`:** The homepage template welcoming the users and displaying a set of instructions that explain to users how to interact with the app.
- **`layout.html`:** The layout template takes advantage of JINJA syntax and the templating system to hold the common HTML information across all the pages, allowing each .html file to only modify the contents inside the body of the page.
- **`login.html`:** The login page template with input fields for the user's username and password.
- **`register.html`:** The registration page template where users create a new account, adhering to the specified rules for username and password.
- **`topColors.html`:** Displays the top three most voted colors on a responsive slideshow. Using JavaScript, extracts the data sent by the **/top** route and changes the color on the slideshow when the user click on the previous or next buttons.
- **`vote.html`:** Allows user to vote for their favorite colors. Users type in the name of their choosen color in an input field, and making asynchronous requests (AJAX) with JavaScript, displays a list of the colors that match the input provided by the user.

#### 5. `database.db`
This SQLite database file stores all the data related to users, colors, and votes. It is dynamically updated as users interact with the application (e.g., submitting colors, voting).


## Usage and Features

After installing, run the web app and submit your favorite colors! Navigate to the homepage and click the "Submit a Color" button to get started.

- **Register:** Register and Log in to be able to use all the user reserved features.
- **Submit a Color:** Fill out the form with your color's name and hex code.
- **Vote for Colors:** View and vote for other submitted colors on the ranking page.

### Features

- User submission of color names and hex codes.
- Color ranking system based on user votes.
- Interactive and responsive design for great user experience on all devices.

### Design Decisions

---

One of the most debated design decisions during the development process was how to handle color name validation. Initially, I allowed for more flexible naming (e.g., special characters and numbers), but after testing, it became apparent that simpler, more traditional names felt more natural for users. We opted for a rule-based validation approach that ensures names are purely alphabetical and have a defined character limit. This makes the app more user-friendly and keeps color names consistent across the platform.

But the most challenging design decision in the development of **ColorCraze** was implementing the vote system. Initially, the goal was to create a simple upvoting mechanism where users could vote for their favorite colors. However, after considering how to keep the app engaging, I decided to introduce a layer of **gamification** by limiting the number of votes a user can cast and creating a system that encourages continuous participation through **vote recharges**. 

#### **Vote Limitation and Recharge Mechanism**

When a new user registers in the app, they start with three votes. These votes are cast on any color of their choosing within the list. Once the user has cast their three votes, they can no longer vote until they recharge their voting allowance. This recharge mechanism is tied to user engagement: *every time a user submits a new color to the list, they receive three additional votes to cast*. This means that to continue voting, users need to stay actively involved by contributing new colors to the community.

The design of this vote system offers several key benefits:
- **Encourages Engagement:** By tying voting to submitting new content, the system encourages users to stay actively involved with the platform. This helps ensure that the app remains dynamic and vibrant, with a steady influx of new colors being added regularly. Users are more motivated to contribute because participation has a direct benefit: more votes.
- **Reduces Spam Voting:** A limited vote system prevents users from indiscriminately upvoting every color. Instead, users must think carefully about which colors truly resonate with them. This ensures that the most popular colors earn their votes based on genuine user appreciation rather than a flood of random votes.
- **Promotes Ownership:** Users have a sense of ownership over their voting decisions. Knowing they only have a limited number of votes makes those votes feel more meaningful and impactful. When they submit a new color to gain more votes, it creates a deeper connection to the content within the app, as they’re not just passive users—they’re actively contributing to the community.
- **Game-Like Incentives:** The vote recharge system introduces a subtle gaming element. It becomes a cycle: submit a new color, earn more votes, and then vote for other users' colors or promote your favorites. This cycle of earning and spending votes mirrors game mechanics often found in apps with point systems, rewarding users for participating in a variety of ways.

#### **Why This System Was Chosen**

When brainstorming ways to encourage engagement, I initially considered allowing users to vote endlessly, with no restrictions on the number of votes they could cast. However, I quickly realized that an unrestricted system would lead to a lack of thoughtful voting and would diminish the value of each individual vote. There was also a risk that, without limitations, some users could over-influence the ranking system by voting excessively for their own submissions or their favorite colors, regardless of quality or popularity.

I considered implementing other systems, such as awarding a set number of daily votes to encourage users to return regularly. However, after reviewing several gamification techniques, I realized that encouraging user-generated content would be more beneficial for ColorCraze in the long run. By requiring users to submit new colors to recharge their voting allowance, the app ensures that users stay engaged both as voters and as contributors, keeping the color list fresh and ever-expanding.

Another reason for choosing this system was to foster a sense of balance in user participation. Rather than allowing passive consumption, the vote-recharge mechanism encourages active contribution. This system adds an extra layer of interactivity by ensuring that users not only engage with the content but also contribute to its creation.

#### **Technical Implementation**

From a technical standpoint, implementing this system required some thoughtful design. Each user has an attribute in the database that stores their remaining votes. When a vote is cast, the application reduces this count by one. Once the count reaches zero, the user is prevented from casting further votes until they submit a new color, at which point their vote count is increased by three.

I used Flask sessions to manage user login states and kept track of each user’s remaining votes via the database. The logic that governs whether a user can vote or not is checked before every vote is submitted to the database. This ensures that users cannot bypass the system and always have the correct number of votes based on their activity. Similarly, when a user submits a new color, the vote count is updated and reflected in real-time, ensuring a seamless experience.

To ensure fairness and consistency, I also introduced server-side validation to check for any inconsistencies between the client and server when voting or submitting colors. This protects against malicious attempts to manipulate the voting system.

The vote system not only adds an element of strategy and fun but also increases the longevity of user engagement within the app. By encouraging users to stay active and submit new colors, ColorCraze fosters a more vibrant and continually evolving community. I believe that this decision will enhance the overall user experience while helping to maintain the integrity of the app’s core features.

### Future Improvements

---

While **ColorCraze** offers a solid foundation for users to submit, vote, and explore colors, there are several opportunities for improving existing features and introducing new functionality to enhance the overall experience. Below are some ideas for potential improvements that would allow for greater personalization, community interaction, and usability, taking the application to the next level:

#### 1. **Enhanced User Profiles**

- **User Color History:** Display a list of colors a user has submitted within their profile.
- **Favorite Colors:** Allow users to "favorite" or bookmark specific colors for easy access in the future.
- **User Avatars:** Let users upload a profile picture to add a personal touch to their accounts.

#### 2. **Color Palette Creation Tool**

- **Custom Palettes:** Allow users to create custom palettes by selecting multiple colors from the existing submissions and grouping them into a cohesive color scheme.
- **Palette Sharing:** Enable users to share their custom palettes with others and receive votes on the best palettes.

#### 3. **Advanced Voting and Rating System**

- **Downvotes:** Introduce downvotes to allow users to indicate their dislike for specific colors, which could influence the color ranking system.

#### 4. **Improved Color Name Validation**

- **Name Suggestions:** If a user submits a color name that already exists, suggest alternative names based on the hue or related colors.

## Contributing

We’d love your help in making this project better! Please feel free to contribute by:

- Reporting any bugs via the [issues page](https://github.com/rdrlaguna/ColorCraze.git).
- Creating pull requests with improvements or bug fixes.
- Suggesting new features!


