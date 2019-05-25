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
