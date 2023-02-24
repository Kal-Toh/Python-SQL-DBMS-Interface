from add_data import select_table
import os
def delete_menu(con, cur, db_name):
    selection = int(input("""
    What would you like to delete?
    1. Record
    2. Table
    3. Database
    4. Back
    """))
    if selection == 1:
        delete_record(con, cur, db_name)
    elif selection == 2:
        delete_table(con, cur, db_name)
    elif selection == 3:
        delete_database(con, cur, db_name)
    elif selection == 4:
        return
    else:
        print("""
    Unrecognised selection.""")


def delete_record(con, cur, db_name):
    table_name = select_table(con, cur, db_name, cont="delete")
    print(f"You have selected {table_name}")
    record_sel = select_record(con, cur, db_name, table_name)
    confirm = input(f"Are you sure you wish to delete {record_sel[0]} from {table_name}? This cannot be undone. y/n:\n")
    if confirm =="y":
        cur.execute(f"PRAGMA table_info({table_name})")
        columns = cur.fetchall()
        column_names = [i[1] for i in columns]
        sql_code = f"DELETE FROM {table_name} WHERE {column_names[0]}='{record_sel[1][0][0]}';"
        cur.execute(sql_code)
        con.commit()
        print(f"{record_sel[0]} deleted from {table_name}.")
    else:
        print("Deletion Canceled.")
    
    #del menu

def select_record(con, cur, db_name, table_name):
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    if rows:
        for i, row in enumerate(rows):
            print(f"{i+1}. {row}")
        row_sel = int(input(f"Select row to delete in '{table_name}':\n")) #TODO Select multiple rows, if rows are over 25 ???
    else:
        print(f"No data found in table '{table_name}'.")
    return rows[row_sel-1], rows

def delete_table(con, cur, db_name):
    table_name = select_table(con, cur, db_name, cont="delete")
    view = input(f"You have selected {table_name}. Would you like to view table data before continuing? y/n:\n")
    if view == "y":
            cur.execute(f"SELECT * FROM {table_name}")
            rows = cur.fetchall()
            if rows:
                print(f"Data in table '{table_name}':")
                for row in rows:
                    print(row)
            else:
                print(f"No data found in table '{table_name}'.")
    confirm = input(f"Are you sure you wish to delete {table_name} from {db_name}? This will delete all records and cannot be undone. y/n:\n")
    if confirm =="y":
        sql_code = f"DROP TABLE {table_name}"
        cur.execute(sql_code)
        con.commit()
        print(f"{table_name} deleted.")

def table_rec_count(con, cur, db_name):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    if tables == []:
        return ("000")
    else:
        # table_list = "\n    ".join([f"{i+1}. {f}" for i, f in enumerate(tables)])
        # return table_list
        table_rec_count = []
        for table in tables:
            cur.execute(f"SELECT COUNT(*) FROM {table[0]};")
            count = cur.fetchone()[0]
            table_rec_count.append((count))
    return tables, table_rec_count

def delete_database(con, cur, db_name):
    print("WARNING: THIS WILL DELETE ALL TABLES AND RECORDS FROM THIS DATABASE. THIS CANNOT BE UNDONE.")
    tab_count = table_rec_count(con, cur, db_name)
    table_list = [table[0] for table in tab_count[0]]
    tab_rec_list = tab_count[1]
    rec_count = [f"{table} with {count} records" for table, count in zip(table_list, tab_rec_list)]
    print(f"""
    You are currently using {db_name}.
    This database contains:
    {' | '.join(rec_count)}
    """)
    confirm = input(f"""Are you sure you wish to permanently delete this database and its associated records?
    Please type the database name: {db_name} to continue.\n""")
    if confirm == db_name:
        os.remove(db_name)
        print(f"\nDatabase {db_name} deleted.")
        con.close()
        from main import start
        start()

        
    #show contents
    #confirm by typing database name
    #delete
    #del menu