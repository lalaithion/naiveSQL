#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

try:
    c.execute('''DROP TABLE users''')
except Exception:
    pass

c.execute('''CREATE TABLE users
             (email text, password text, name text, admin int)''')

c.execute('''INSERT INTO users VALUES ('izaak@fake.com','swordfish','Izaak Weiss', 0)''')
c.execute('''INSERT INTO users VALUES ('alex@fake.com','papyrus','Alex Curtiss', 0)''')
c.execute('''INSERT INTO users VALUES ('beyonce@fake.com','singlelady','Beyonce', 0)''')
c.execute('''INSERT INTO users VALUES ('grace@fake.com','FLOWMATIC','Grace Hopper', 1)''')

conn.commit()
conn.close()
