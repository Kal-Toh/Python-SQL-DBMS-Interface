<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/kal-toh/python-sql-dbms-interface">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">PyDMBSI</h3>

  <p align="center">
    A Python interface for database management.
    <br />
    <a href="https://github.com/kal-toh/python-sql-dbms-interface"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/kal-toh/python-sql-dbms-interface">View Demo</a>
    · -->
    <a href="https://github.com/kal-toh/python-sql-dbms-interface/issues">Report Bug</a>
    ·
    <a href="https://github.com/kal-toh/python-sql-dbms-interface/issues">Request Feature</a>
  </p>
</div>

## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This program provides a command line menu based interface for interacting with an SQL database. Users can select an existing database or create either a new database a database, either empty or filled data scraped from the web.

Once a database is selected, the user is presented with a menu of operations to perform on the database:

1. View Data
2. Add Data
3. Update Data
4. Delete Data

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

Whilst PyDBMSI is still under development it can be cloned via GitHub and ran with main.py.

### Prerequisites

- beautifulsoup4
  ```sh
  pip install beautifulsoup4
  ```
- pandas
  ```sh
  pip install pandas
  ```
- requests
  ```sh
  pip install requests
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kal-toh/python-sql-dbms-interface.git
   ```
2. Install prerequisite
   ```sh
   pip install -r requirements.txt
   ```
3. Locate folder in terminal and run `main.py` in python
   ```sh
   python main.py
   ```
   Alternatively, you can open the main.py file in your preferred Python IDE and run it from there.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

PyDBMSI can be used to interact with an existing SQL database or create a new one.

To use an existing database place the `database.db` file into the cloned directory.

Current functions include: Viewing tables and data, adding tables and data, scraping tables from HTML based websites, updating data and deleting tables, data and databases.

All functions can easily be accessed via the easy to navigate command line menu.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- ✅ Importing data from Web
  - [ ] Importing data multiple web pages simultaneously
- [ ] Importing data from CSV
- [ ] Exporting data to CSV
- [ ] Sorting, aggregation and visualisation of data

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## More Links

[Personal Website](https://roryohlmeier.com) - [@kadiskot](https://twitter.com/kadiskot)

Project Link: [https://github.com/kal-toh/python-sql-dbms-interface](https://github.com/kal-toh/python-sql-dbms-interface)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
