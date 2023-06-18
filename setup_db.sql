-- A MySql script that prapares a MySQl server for the project

CREATE DATABASE IF NOT EXISTS gitfolio_db;
CREATE USER IF NOT EXISTS 'gitfolio_dev'@'localhost' IDENTIFIED BY 'gitfolio_pwd';
GRANT ALL PRIVILEGES ON gitfolio_db.* TO 'gitfolio_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'gitfolio_dev'@'localhost';
