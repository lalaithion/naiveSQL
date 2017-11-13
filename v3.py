#!/usr/bin/env python3

import MySQLdb
import readline
import hashlib

from tabulate import tabulate

conn = MySQLdb.connect(user="hacking", passwd="password", db="ethical")

def md5(password):
    hsh = hashlib.md5(password.encode('utf-8')).digest()
    return ''.join(map(chr, hsh))

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
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        logged_in = validate(email, md5(password))

    print("[A]dd new user, [L]ist all users, [W]ho am I, [Q]uit")

    while True:
        action = input("> ")
        if action == 'A':
            if is_admin(email):
                newemail = input("Enter the new user's email address: ")
                newpass = input("Enter the new user's password: ")
                newname = input("Enter the new user's name: ")
                isadmin = input("Enter 1 if the user is an admin, or 0 otherwise: ")
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
