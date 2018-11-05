# MAC5853 Desenvolvimento de Sistemas de Computacao

## Overview

## Requirements
* Flask
* MySQL

mysql -u root
* CREATE USER 'db_admin'@'localhost' IDENTIFIED BY 'dbadmin'
* CREATE DATABASE dsvdb;
* GRANT ALL PRIVILEGES ON dsvdb . * TO 'db_admin'@'localhost';

## Usage

First, start the Flask server

```bash
cd MAC5853-Desenvolvimento-de-Sistemas-de-Computacao
export FLASK_APP=flaskr
flask run
* Serving Flask app "flaskr"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Then, send a POST HTTP request to http://127.0.0.1:5000/ with JSON data containing the
sites to be processed and the callback URL.

