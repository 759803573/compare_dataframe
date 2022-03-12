CREATE DATABASE source_db CHARACTER SET utf8mb4;
CREATE TABLE source_db.source_table (
  f1 int,
  f2 varchar(255),
  f3 int
);
INSERT INTO source_db.source_table (f1, f2, f3) VALUES (1, 'key1', 1);
INSERT INTO source_db.source_table (f1, f2, f3) VALUES (2, 'key2', 2);
INSERT INTO source_db.source_table (f1, f2, f3) VALUES (3, 'key3', 3);
