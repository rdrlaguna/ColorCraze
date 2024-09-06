# Schema for the project's database

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    date TEXT NOT NULL,
    votes INTEGER NOT NULL DEFAULT 3
);

CREATE UNIQUE INDEX username ON users (username);


CREATE TABLE colors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    color_name TEXT NOT NULL,
    hex TEXT NOT NULL,
    red INTEGER NOT NULL,
    green INTEGER NOT NULL,
    blue INTEGER NOT NULL,
    hue INTEGER NOT NULL,
    saturation INTEGER NOT NULL,
    light INTEGER NOT NULL,
    date TEXT NOT NULL,
    hour TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE UNIQUE INDEX color_name ON colors (color_name);

CREATE UNIQUE INDEX  hex ON colors (hex);

CREATE TABLE voted_colors (
    user_id INTEGER NOT NULL,
    color_id INTEGER NOT NULL,
    votes INTEGER NOT NULL DEFAULT 0,
    date TEXT NOT NULL,
    hour TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(color_id) REFERENCES colors(id)
);


-- Insert vote's id in votes TABLE
-- Add user registration date