
https://docs.google.com/presentation/d/1HIWHeXisW_nc5KHOJ0DlhZeW9lXxSeoU0WC5lf2lgSo/edit#slide=id.p
B


## Overview

## Requirements
* Flask
* flask_sqlalchemy
* flask_migrate
* flask_restful
* MySQL

## Database Setup
Logon to mysql -u root and use the next commands:
* CREATE USER 'db_admin'@'localhost' IDENTIFIED BY 'dbadmin';
* CREATE DATABASE dsvdb;
* GRANT ALL PRIVILEGES ON dsvdb . * TO 'db_admin'@'localhost';

Then use
```bash
cd MAC5853-Desenvolvimento-de-Sistemas-de-Computacao
* flask db init
* flask db migrate
* flask db upgrade
```
## Usage

First, start the Flask server

```bash
export FLASK_APP=flaskr
flask run
* Serving Flask app "flaskr"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Then, send a POST HTTP request to http://127.0.0.1:5000/ with JSON data containing the
sites to be processed and the callback URL.


### Project Description
This is a project to identify that sites are good according to certain policies.

UPDATE 05/11: All the data model classes were created. And a CRUD resource and unit tests for it were implemented. We will replicate this for the remaining
classes and then we will finish creating the machine learning models and other rules.
