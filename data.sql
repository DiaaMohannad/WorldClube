CREATE TABLE country (
    id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);
CREATE TABLE customs (
    id INTEGER PRIMARY KEY ,
    country_id INTEGER NOT NULL,
    tradition TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (country_id) REFERENCES country(id)
);
CREATE TABLE events (
    id INTEGER PRIMARY KEY ,
    customs_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (customs_id) REFERENCES customs(id)
);
CREATE TABLE food (
    id INTEGER PRIMARY KEY ,
    customs_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (customs_id) REFERENCES customs(id)
);