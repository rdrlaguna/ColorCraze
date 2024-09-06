# ColorCraze
Web app to list and vote for all your favorite colors.

## Description

A short description of what your project does, why it’s important, and any key features. For example:

This is a Python Flask web app that allows users to submit and vote on colors, showcasing the most popular user-submitted colors. It’s a fun and interactive way for users to engage with color theory while practicing web development.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [Tests](#tests)
- [License](#license)
- [Authors and Acknowledgments](#authors-and-acknowledgments)

## Installation

### Prerequisites

- Python 3.8+
- Flask
- SQLite (optional, or replace with your preferred DBMS)

### Installation Steps

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

## Usage

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

