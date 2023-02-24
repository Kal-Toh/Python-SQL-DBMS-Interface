from view_database import read
from add_data import select_table
def update(con, cur, db_name):
    if read(con, cur, db_name, cont=False) == False:
        print("Database Empty. Add a song first.")
        return
    else:
        table_name = select_table(con, cur, db_name, cont="update")[3]
        select_row(con, cur, db_name, table_name)

def select_row(con, cur, db_name, table_name, cont="update"):
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    if rows:
        for i, row in enumerate(rows):
            print(f"{i+1}. {row}")
        row_sel = int(input(f"Select row to update in '{table_name}':\n")) #TODO Select multiple rows, if rows are over 25 ???
        print(f"Selected row: \n{rows[row_sel-1]}")
        if cont == "update":
            update_record(con, cur, db_name, table_name, row_sel, rows)
        elif cont == "delete":
            return row_sel, rows
    else:
        print(f"No data found in table '{table_name}'.")

def update_record(con, cur, db_name, table_name, row_sel, rows):
    add_more = True
    while add_more == True:
        cur.execute(f"PRAGMA table_info({table_name})")
        columns = cur.fetchall()
        column_names = [i[1] for i in columns]
        values =[]
        for column in column_names:
                value = input(f"Enter value for {column}: ")
                values.append(value)
        sql_string =[]
        for (col, val) in zip(column_names, values):
            string = f'{col} = "{val}"'
            sql_string.append(string)
        confirm = input(f"""
        This will change:\n{rows[row_sel-1]} to \n({', '.join(values)})\n Continue? y/n:\n
        """)
        if confirm =="y":
            sql_code = f"UPDATE {table_name} SET {', '.join(sql_string)} WHERE {column_names[0]}='{rows[row_sel-1][0]}';"
        cur.execute(sql_code)
        con.commit()
        add_ask = input(f"Row updated. Update more? y/n\n")
        if add_ask =="y":
            add_more = True
        else:
            add_more = False

# UPDATE desert SET food = "foofoo", calories = "2020", chocolate = "no" WHERE food=Cake
