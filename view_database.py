import time
from tabulate import tabulate

def read(con, cur, db_name, cont=True):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    if tables == []:
        print("The database is empty.")
        return False
    else:
        if cont == True:
            read_select(con, cur, db_name, tables)
        
            return True,

def read_select(con, cur, db_name, tables):
    table_list = "\n    ".join([f"{i+1}. {f}" for i, f in enumerate(tables)])
    time.sleep(0.2)
    table_selection = int(input(f"""
    Select a table:
    {table_list}
    """)) - 1
    view_table(con, cur, db_name, table_selection, tables, table_list)

def view_table(con, cur, db_name, table_selection, tables, table_list):
    table_name = tables[table_selection]
    table_name_str = str(table_name)
    table_name_clean = table_name_str[2:-3]
    cur.execute(f"SELECT * FROM {table_name_clean}")
    rows = cur.fetchall()
    if rows:
        print(f"Data in table '{table_name_clean}':")
        for row in rows:
            print(row)
    else:
        print(f"No data found in table '{table_name_clean}'.")

def view_table(con, cur, db_name, table_selection, tables, table_list):
    table_name = tables[table_selection]
    table_name_str = str(table_name)
    table_name_clean = table_name_str[2:-3]
    cur.execute(f"SELECT * FROM {table_name_clean}")
    rows = cur.fetchall()
    if rows:
        cur.execute(f"Select * FROM {table_name_clean} LIMIT 0")
        headers = [desc[0] for desc in cur.description]
        print(f"\nData in table '{table_name_clean}':\n")
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid', maxcolwidths=23))
    else:
        print(f"No data found in table '{table_name_clean}'.")
    



