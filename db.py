import sqlite3

#   Create SQLITE connection
connection = sqlite3.connect('local.db')


#   Execute Users table initialisation SQL
with open('init.sql') as f:
    connection.executescript(f.read())

connection.close()
