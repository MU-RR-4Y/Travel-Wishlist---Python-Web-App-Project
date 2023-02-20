DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS destinations;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    
);

CREATE TABLE destinations(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    information VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
 );
 


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE visits(
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
    date VARCHAR(225),
    rating INT,
    comment VARCHAR(255)

);

