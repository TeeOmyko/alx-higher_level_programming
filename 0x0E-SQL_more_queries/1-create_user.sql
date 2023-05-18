-- creates a database and the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
