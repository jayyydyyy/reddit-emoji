CREATE DATABASE reddit;
ALTER DATABASE reddit CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use reddit;

CREATE TABLE post (
    id VARCHAR(10) NOT NULL,
    title TEXT,
    text_field TEXT,
    subreddit TEXT,
    time_posted INT(11),
    PRIMARY KEY (id)
);

CREATE TABLE comment (
    id VARCHAR(10) NOT NULL,
    post_id VARCHAR(10) NOT NULL,
    text_field TEXT,
    subreddit TEXT,
    time_posted INT(11),
    PRIMARY KEY (id),
    FOREIGN KEY (post_id) REFERENCES post (id)
);