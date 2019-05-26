-- --------------------------------------------
-- books
-- --------------------------------------------
DROP TABLE IF EXISTS books;

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  isbn VARCHAR(20),
  title VARCHAR(255),
  author VARCHAR(100),
  year INT
);

ALTER SEQUENCE books_id_seq RESTART WITH 1001;

-- --------------------------------------------
-- users
-- --------------------------------------------
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50),
  password_hash VARCHAR(255),
  email VARCHAR(255)
);

ALTER SEQUENCE users_id_seq RESTART WITH 101;

-- --------------------------------------------
-- book reviews
-- --------------------------------------------
DROP TABLE IF EXISTS book_reviews;

CREATE TABLE book_reviews (
  id SERIAL PRIMARY KEY,
  book_id INT REFERENCES books(id) ON DELETE CASCADE,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  review TEXT,
  rating INT
);

