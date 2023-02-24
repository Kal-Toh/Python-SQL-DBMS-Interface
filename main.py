from os import listdir
import time
from create_db import create_new_db
import sqlite3 as sql
from view_database import read
from add_data import *
from update_data import *
from delete_data import *

#TODO - Make sure menu text inline
#TODO - Make sure sleep timing is used throughout modules 
#TODO - Add options to return to previous menu
#TODO - Remove symbols from pulled data
#TODO - Display data in more table like fashion
#TODO - Add sorting for data, maybe visualise?
#TODO - Add option to export tables to other formats
con = None
db_name = None
def start():
    print(f"""
    Welcome to PyDBMS.
    """)
    db_files = [f for f in listdir() if f.endswith(".db")]
    db_list = "\n".join([f"{i+1}. {f}" for i, f in enumerate(db_files)])
    if db_files:
        time.sleep(0.2)
        selection = input(f"""
    Databases found: {", ".join(db_files)}

    Would you like to select an existing database? y/n:\n
    """)
        if selection == "y":
            time.sleep(0.2)
            db_selection = int(input(f"""
            Select a database:
            {db_list}
            """)) - 1
            db_name = db_files[db_selection]
            con = sql.connect(db_name)
            return con, db_name
            
        elif selection == "n":
            return create_new_db()
        else:
            time.sleep(0.2)
            print("Unrecognised selection.")
            start()
            #! Make while loop.
    else:
        time.sleep(0.2)
        selection = input(f"""
    No databases found, would you like to create one? y/n:\n
    """)
        if selection == "y":
            time.sleep(0.2)
            return create_new_db()
        elif selection == "n":
            time.sleep(0.2)
            print("Closing.")
        else:
            time.sleep(0.2)
            print("Unrecognised selection.")
            start()


    
def db_operations():
    time.sleep(0.2)
    print(f"""
    Using {db_name} with PyDBMS:
    """)
    time.sleep(0.2)
    selection = input(f"""
    Select an operation:
    1. View Data
    2. Add Data
    3. Update Data
    4. Delete Data
    5. Exit
    """)
    if selection == "1":
        time.sleep(0.2)
        read(con, cur, db_name)
    elif selection =="2":
        time.sleep(0.2)
        add_data_mu(con, cur, db_name)
    elif selection =="3":
        time.sleep(0.2)
        update(con, cur, db_name)
    elif selection =="4":
        time.sleep(0.02)
        delete_menu(con, cur, db_name)

        
    
    else:
        print("Not yet implemented.")

while con == None:
    con, db_name = start()
cur = con.cursor()
while con != None:
    db_operations()