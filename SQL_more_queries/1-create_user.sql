-- Delete user named user_0d_1 if exists and create a it with all privileges
DROP USER IF EXISTS 'user_0d_1'@'localhost'; CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;