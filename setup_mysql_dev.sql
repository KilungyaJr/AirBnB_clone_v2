-- This script prepares mysql server for the project
-- first create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- New user in localhost with password.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Set privilege of the a specific database.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- User 'hbnb_dev' should have all privileges on db 'hbnb_dev_db'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
