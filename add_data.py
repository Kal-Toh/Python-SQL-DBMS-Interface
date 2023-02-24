import time
from view_database import read_select
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
def add_data_mu(con, cur, db_name):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    if tables == []:
        emp_tbl = input("""
        No tables found, would you like to add one? y/n:\n
        """)
        if emp_tbl == "y":
            add_tbl_(con, cur, db_name)
    else:
        add_type = input("""
        What would you like to add?
        1. Table
        2. Data
        """)
        if add_type == "1":
            add_tbl_(con, cur, db_name)
        elif add_type == "2":
            select_table(con, cur, db_name)

def add_tbl_(con, cur, db_name):
    print("""
        How would you like to table?
            """)
    selection = input("""
        1. Manually
        2. From Web
        3. From CSV file
            """)
    if selection == "1":
        add_manual_table(con, cur, db_name)
    elif selection == "2":
        add_web_table(con, cur, db_name)

def add_manual_table(con, cur, db_name):
    add_more = "y"
    new_tables =[]
    table_name = input("""
    Enter table name:\n""")
    while add_more == "y":
        column_name = input("""
    Enter column name:\n""")
        data_type = input(f"""
    Enter data type for {column_name}:\n""")
        constraint = input(f"""
    Enter constraint for {column_name} or leave blank:\n""")
        new_tables.append(f"{column_name} {data_type} {constraint}")

        add_more = input("""
        Would you like to add another column? y/n: \n
        """)
    sql_code = f"CREATE TABLE {table_name} ({', '.join(new_tables)})"

    confirm = input(f"""
    Are you sure you want to create '{table_name}' with {new_tables} y/n:\n?
    """)
    if confirm == "y":
        cur.execute(sql_code)
        con.commit()
    #! ELSE TABLES NOT EMPTY

def select_table(con, cur, db_name, cont="add"):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    if tables == []:
        print("The database is empty.")
    else:
        table_list = "\n    ".join([f"{i+1}. {f}" for i, f in enumerate(tables)])
        time.sleep(0.2)
        table_selection = int(input(f"""
    Select a table:
    {table_list}
    """)) - 1
    table_name = tables[table_selection]
    table_name_str = str(table_name)
    table_name_clean = table_name_str[2:-3]
    if cont == "add":
        add_data(con, cur, db_name, table_name_clean)
    elif cont=="update":
        return 
    elif cont=="delete":
        return table_name_clean

def add_data(con, cur, db_name, table_name_clean):
    print(f"""
        How would you like to data to {table_name_clean}?
            """)
    selection = input("""
        1. Manually
        2. From Web
        3. From CSV file
            """)
    if selection == "1":
        add_manual_data(con, cur, db_name, table_name_clean)

def add_manual_data(con, cur, db_name, table_name_clean):
    add_more = True
    while add_more == True:
        cur.execute(f"PRAGMA table_info({table_name_clean})")
        columns = cur.fetchall()
        column_names = [i[1] for i in columns]
        values = []
        print(f"""
        Column names in {table_name_clean}: {column_names}
        """)
        for column in column_names:
            value = input(f"Enter value for {column}: ")
            values.append(value)
        sql_code = f"INSERT INTO {table_name_clean} ({', '.join(column_names)}) VALUES ({', '.join(['?' for _ in column_names])})"
        confirm = input(f"""
        Are you sure you want to add:
        {column_names}
        {values}
        to {table_name_clean}? y/n\n
        """)
        if confirm =="y":
            cur.execute(sql_code, values)
            con.commit()
            print(f"Data added to {table_name_clean}")
        ask_more = input(f"""
        Would you like to add more data to {table_name_clean}? y/n\n
        """)
        if ask_more == "y": 
            add_more = True 
        else: add_more = False

def add_web_table(con, cur, db_name):
    url = input("""
    Enter URL of page you would like to scrape for data. The data must be formatted in HTML.\n
    """)
    scraped_data = scrape_web_data(url)
    if scraped_data:
        table_name = input("""
    Data scraped. Enter a name for your table.\n
        """)
        column_names = scraped_data[1]
        column_names_clean = []
        for dirt in column_names:
            cleaned = re.sub(r'\W+','_',dirt)
            column_names_clean.append(cleaned)
        new_table = []
        for column in column_names_clean:
            data_type = input(f"Enter data type for {column}:\n")
            constraint = input(f"Enter constraint for {column} or leave blank\n")
            new_table.append(f"{column} {data_type} {constraint}")
        sql_code = f"CREATE TABLE {table_name} ({', '.join(new_table)})"
        
        cur.execute(sql_code)

        add_data = input("Would you like to add scraped data to this table? y/n\n")
        if add_data == "y":
            for row in scraped_data[0].itertuples(index=False):
                values_dirty = [str(value).replace("'", " ") for value in row]
                values = ", ".join(f"'{str(value)}'" for value in values_dirty)
                sql_code = f"INSERT INTO {table_name} VALUES ({values});"
                cur.execute(sql_code)
                con.commit()
                print(f"Scraped data inserted into {table_name}")
        elif add_data == "n":
            con.commit()
            print(f"{table_name} created.")
            #! USE interpolation
            #! Add count of records added


def scrape_web_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table_eml = soup.find('table')
    headers = []
    for i in table_eml.find_all('th'):
        title = i.text
        headers.append(title)
    data = pd.DataFrame(columns=headers)
    for i in table_eml.find_all('tr')[1:]:
        row_data = i.find_all('td')
        if len(row_data) == len(headers):
            row = [i.text for i in row_data]
            length = len(data)
            data.loc[length] = row
    return data, headers

