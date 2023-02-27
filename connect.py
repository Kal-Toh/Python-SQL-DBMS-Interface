import sqlite3 as sql

def create_db(database_name):
    return sql.connect(f"{database_name}.db")

con = sql.connect("")
cur = con.cursor()