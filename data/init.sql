CREATE DATABASE reddit;
ALTER DATABASE reddit CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use reddit;

CREATE TABLE post (
    id VARCHAR(128) NOT NULL,
    title TEXT,
    text_field TEXT,
    subreddit TEXT,
    time_posted INT(11),
    PRIMARY KEY (id)
);

CREATE TABLE comment (
    id VARCHAR(128) NOT NULL,
    post_id VARCHAR(128) NOT NULL,
    text_field TEXT,
    subreddit TEXT,
    time_posted INT(11),
    PRIMARY KEY (id),
    FOREIGN KEY (post_id) REFERENCES post (id)
);