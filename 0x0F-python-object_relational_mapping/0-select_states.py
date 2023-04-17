#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa """
"""
This script uses the MySQLdb module to connect to a MySQL server and list all states from a database.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # Create a cursor to execute SQL queries
    cur = db.cursor()
    # Execute the SQL query to select all states from the database
    cur.execute("SELECT * FROM states")
    # Fetch all the rows returned by the SQL query
    rows = cur.fetchall()
    # Print the results in the specified format
    for row in rows:
        print(row)
    # Close the cursor and database connections    
    cur.close()
    db.close()
