# naiveSQL

This is meant as a teaching tool about SQL vulnerabilities. THIS IS NOT A
PROJECT YOU SHOULD IMITATE FOR ACTUAL DATABASE MANAGEMENT

This project creates a simple User database, and provides a naive command
line interface for working with the database. v1.py is a very insecure
interface; subsequent versions are more complex

## Requirements

Install MySQL. Create a database called `ethical`, and a user with username `hacking`, and password `password`.

Run `pip3 install mysqlclient`.

## Instructions

Use `./setup.py` or `python3 setup.py` to configure the database.

Then, use `./v1.py` or `python3 v1.py` to interact with, and attempt to
break into, this SQL application.
