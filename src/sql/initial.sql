DROP DATABASE IF EXISTS theater;
CREATE DATABASE theater;
USE theater;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL

);
-- INSERT INTO users (username, password)
-- VALUES ("ali", "leyla"),
--     ("karimi", "sakht");
CREATE TABLE salons(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    parkinglot BIT DEFAULT 0,
    srow INT,
    scolumn INT,
    extra INT DEFAULT 0
);
-- INSERT INTO salons (name, address, srow, scolumn)
-- VALUES ("azadi", "abbas-abad", 10, 7);
CREATE TABLE shows (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    director_id INT NOT NULL,
    genre VARCHAR(255) NOT NULL,
    date_time DATETIME NOT NULL,
    place_id INT NOT NULL,
    duration TIME,
    FOREIGN KEY (director_id) REFERENCES users(id),
    FOREIGN KEY (place_id) REFERENCES salons(id)
);
-- INSERT INTO shows (
--         name,
--         director_id,
--         genre,
--         date_time,
--         place_id,
--         duration
--     )
-- VALUES ("madar", 1, "drama", now(), 1, "90:00");
CREATE TABLE tickets(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    show_id INT NOT NULL,
    n0 INT NOT NULL,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
-- INSERT INTO tickets (user_id, show_id, n0)
-- VALUES (2, 1, 5),
--     (2, 1, 6);
