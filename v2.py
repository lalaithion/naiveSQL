#!/usr/bin/env python3

import MySQLdb
import readline

from tabulate import tabulate

conn = MySQLdb.connect(user="hacking", passwd="password", db="ethical")

def clean_input(s=""):
    string = input(s)
    string = string.replace("\\", "\\\\")
    string = string.replace("'", "''")
    return string

def validate(email, password):
    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM users WHERE email='{}' AND password='{}';".format(email, password)
    )
    name = cur.fetchone() # Returns None if there is nothing
    return name

def is_admin(email):
    cur = conn.cursor()
    cur.execute(
        "SELECT admin FROM users WHERE email='{}';".format(email)
    )
    admin = cur.fetchone()
    return admin[0]

def add_user(email, password, name, admin):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users VALUES ('{}','{}','{}',{});".format(email, password, name, admin)
    )
    conn.commit()

def get_users():
    cur = conn.cursor()
    cur.execute("SELECT email, name FROM users;")
    return cur.fetchall()

def main():
    logged_in = False

    while not logged_in:
        email = clean_input("Enter your email: ")
        password = clean_input("Enter your password: ")
        logged_in = validate(email, password)

    print("[A]dd new user, [L]ist all users, [W]ho am I, [Q]uit")

    while True:
        action = clean_input("> ")
        if action == 'A':
            if is_admin(email):
                newemail = clean_input("Enter the new user's email address: ")
                newpass = clean_input("Enter the new user's password: ")
                newname = clean_input("Enter the new user's name: ")
                isadmin = clean_input("Enter 1 if the user is an admin, or 0 otherwise: ")
                add_user(newemail, newpass, newname, isadmin)
            else:
                print("Only administrators may add new users")
        elif action == 'L':
            print(tabulate(get_users()))
        elif action == 'W':
            print(logged_in[0])
        elif action == 'Q':
            break
        else:
            print("Please enter a valid option: [A]dd new user, [L]ist all users, [W]ho am I, [Q]uit")

if __name__ == "__main__":
    main()
