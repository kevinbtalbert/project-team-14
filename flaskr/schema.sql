DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    id        INTEGER PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName  TEXT NOT NULL
);