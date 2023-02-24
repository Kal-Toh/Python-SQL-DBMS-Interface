import time
from connect import create_db
import sqlite3 as sql

def create_new_db():
    db_name = False
    while db_name == False:
        time.sleep(0.2)
        db_name_set = input("""
    What would you like to name your database?:\n""")+".db"
        db_name_confirm = input(f"""
    Are you sure you would like to name your database '{db_name_set}'? This cannot be changed. y/n \n""")
        if db_name_confirm == "y":
            db_name = db_name_set
            con = sql.connect(db_name)
            return con, db_name
        elif db_name_confirm == "n":
            db_name = False
        else:
            time.sleep(0.2)
            print("Unrecognised selection.")
            db_name = False
