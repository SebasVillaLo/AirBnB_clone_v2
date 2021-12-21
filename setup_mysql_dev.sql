-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'IDENTIFIED BY hbnb_dev_pwd;
<<<<<<< HEAD
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
=======
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@ 'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@ 'localhost';
>>>>>>> bd1947cb5a62e888fe5f76702d54943a91800e61
