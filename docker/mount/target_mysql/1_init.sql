CREATE DATABASE target_db CHARACTER SET utf8mb4;
CREATE TABLE target_db.target_table (
  f1 int,
  f2 varchar(255),
  f3 int
);
INSERT INTO target_db.target_table (f1, f2, f3) VALUES (4, 'key4', 4);
INSERT INTO target_db.target_table (f1, f2, f3) VALUES (2, 'key2', 2);
INSERT INTO target_db.target_table (f1, f2, f3) VALUES (3, 'key4', 3);
