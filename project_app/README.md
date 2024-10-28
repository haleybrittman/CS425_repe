# Transit System Application README

## Requirements
IDE Application (VScode, Eclipse)
Python Installation
SQL connector installation
MYSQL Workbench (Optional)

## Introduction
This project aims to allow users to easily create, read, update, and delete information in the transit system database utilizing SQL-based queries through the command line interface. The application allows users to access each of these functions by interacting with the menu. Error handling is implemented to create a seamless interaction between the user and the application.

## Setup & Database Generation
Download the project_app folder. Transit_system.sql is an SQL script that can be executed to create the database. The script can be executed in MYSQL Workbench. After creating a local instance, go to File > Run SQL Script or File > Open SQL Script. Select the “transit_system.sql” file to execute it. Execute it as a query if you selected “Open SQL script.” 

Alternatively (for Windows):
In the command prompt, change the directory to the project_app directory. Input the following command into the command line and enter your password: 
mysql -u root -p -e "source transit_system.sql"

From here, the Python application can be executed.

## Notes:
Transit_system.sql will drop databases of the same name, allowing users to quickly renew the database.

The host is localhost, name is root. Other hosts and names need to be changed in the Python program.

Be sure that you properly imported the SQL connector in your IDE. Otherwise, you may encounter an error. How to install the connector may vary, but you should be able to install using the command prompt on your computer. Type “pip install mysql-connector-p” and hit enter. It should be installed now. Refer back to your IDE and retry the import.




## Features/Menu options:

Reading Data:
This method allows the user to read data from the schema (tables). It utilizes a select query and returns all the data from the database from tables 1-14.

Inserting Data:
Allows users to insert data in tables 1-14. 

Updating Data:
Allows users to update data in rows of any table

Deleting Data:
Allows for the deleting of rows from a specified table based on user input.





## Contributors:
Zachariah Watson
Haley Brittman

