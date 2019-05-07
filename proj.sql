CREATE SCHEMA project1;
CREATE TABLE project1.artist (
	artist_id INTEGER PRIMARY KEY,
	artist_name VARCHAR(255)
);


CREATE TABLE project1.token (
	song_id INTEGER,
	token VARCHAR(255),
	count INTEGER,
	PRIMARY KEY (song_id, token)
);

CREATE TABLE project1.song (
	song_id INTEGER PRIMARY KEY,
	artist_id INTEGER REFERENCES artist(artist_id),
	song_name VARCHAR(255),
	page_link VARCHAR(1000)
	/* , FOREIGN KEY (artist_id) REFERENCES artist (artist_id) */
);

CREATE TABLE project1.tfidf (
	song_id INTEGER,
	token VARCHAR(255),
	score FLOAT,
	PRIMARY KEY(song_id, token)
);

\copy project1.artist FROM '/home/cs143/data/artist.csv' DELIMITER ',' QUOTE '"' CSV;
\copy project1.song   FROM '/home/cs143/data/song.csv'   DELIMITER ',' QUOTE '"' CSV;
\copy project1.token  FROM '/home/cs143/data/token.csv'  DELIMITER ',' QUOTE '"' CSV;
