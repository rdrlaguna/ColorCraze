# ColorCraze
Web app to list and vote for all your favorite colors.

#### Visit the web:  <https://rodrigolaguna.pythonanywhere.com/>

## Description

Welcome to **ColorCraze**, an interactive web application that allows users to explore, submit, and vote on a variety of custom colors. The app serves as a vibrant community for color enthusiasts to submit unique color hues, give them creative names, and cast votes to create a dynamic ranking of the most popular colors. Whether you're a designer looking for inspiration or just a lover of color, ColorCraze offers an engaging and playful way to interact with the world of color.

This project was developed as the final assignment for **cs50x: Introduction to Computer Science**. The primary goal of the project was to demonstrate the acquired knowledge of modern web technologies like **Python**, **Flask**, **HTML**, **CSS**, **JavaScript**, and **SQL**. The application features *user authentication*, *submission validation*, *dynamic ranking*, and *error handling*, making it a comprehensive project that showcases full-stack development skills.

## Table of Contents
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [Tests](#tests)
- [License](#license)
- [Authors and Acknowledgments](#authors-and-acknowledgments)

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
    source env/bin/activate  # On Windows use `env\Scripts\activate`
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

The repository is organized as follows, allowing for easy addition of future projects.

``` bash
ColorCraze/
├── LICENSE          # License file at the root level
├── README.md        # Repository description
├── static/            # First creative coding project
│   ├── index.html   # Main HTML file
│   ├── script.js    # JavaScript code for the animation
│   ├── styles.css   # Optional styling (if needed)
│   └── assets/      # Folder for images and resources
├── templates/            # First creative coding project
└── other-projects/  # Placeholder for future projects


```

## 3. Usage

After installing, run the web app and submit your favorite colors! Navigate to the homepage and click the "Submit a Color" button to get started.

- **Submit a Color:** Fill out the form with your color's name and hex code.
- **Vote for Colors:** View and vote for other submitted colors on the ranking page.
  

## Features

- User submission of color names and hex codes.
- Color ranking system based on user votes.
- Interactive and responsive design for great user experience on all devices.

## Contributing

We’d love your help in making this project better! Please feel free to contribute by:

- Reporting any bugs via the [issues page](https://github.com/rdrlaguna/ColorCraze.git).
- Creating pull requests with improvements or bug fixes.
- Suggesting new features!

## Tests

Run the tests using:

```bash
pytest
```

