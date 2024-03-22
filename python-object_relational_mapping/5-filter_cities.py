#!/usr/bin/python3
"""
Select state with a name matching a specific pattern
from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connect to a MySQL server
    and select state with a name matching a specific pattern
    using argv and the MySQLdb library
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name\
            FROM `cities`\
            JOIN `states`\
            ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %(state_name)s\
            ORDER BY cities.id ASC",
        {
            'state_name': sys.argv[4]
        }
    )
    rows = cursor.fetchall()
    if rows is not None:
        print(", ".join([city[1] for city in rows]))
    cursor.close()
    db.close()
