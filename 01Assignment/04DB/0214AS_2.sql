-- #1
CREATE TABLE users (
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100) DEFAULT NULL,
    country VARCHAR(100) DEFAULT NULL,
    email VARCHAR(100) DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
    );

-- #2
INSERT INTO
	users (first_name, last_name, birthday, email)
VALUES
	('Beemo', 'Jeong', '1000-01-01', 'beemo@hphk.kr');

INSERT INTO
	users (first_name, last_name, birthday, city, country)
VALUES
	('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea'),
    ('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea'),
    ('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea');

-- #3
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('A', 'A', '1111-01-01', 'A', 'A', 'A@hphk.kr'),
    ('B', 'B', '2222-02-02', 'B', 'B', 'B@hphk.kr'),
    ('C', 'C', '3333-03-03', 'C', 'C', 'C@hphk.kr'),
    ('D', 'D', '4444-04-04', 'D', 'D', 'D@hphk.kr'),
    ('E', 'E', '5555-05-05', 'E', 'E', 'E@hphk.kr');

-- #4
UPDATE
	users
SET
	first_name = 'Soeun',
    last_name = 'Kim',
    birthday = '1996-12-05'
WHERE
	userId = 2;

-- #5
UPDATE
	users
SET
	country = 'Korea'
WHERE
	country IS NULL;

-- country = NULL 아니고 country IS NULL..........

-- #6
DELETE FROM
	users
WHERE
	first_name = 'Beemo';
    
-- #7
DELETE FROM
	users
WHERE
	first_name = 'Kwangsoo'
    AND last_name = 'Lee';
    
-- #8
DELETE FROM
	users
ORDER BY
	created_at DESC
LIMIT 1;