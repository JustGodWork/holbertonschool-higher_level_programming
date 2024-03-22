#!/usr/bin/python3
"""
Select all states from the database hbtn_0e_0_usa
"""

from MySQLdb import connect
import sys

if __name__ == "__main__":
    """
    Connect to a MySQL server
    and list all states in the database
    using argv and the MySQLdb library
    """
    db = connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
