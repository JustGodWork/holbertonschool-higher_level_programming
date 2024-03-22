#!/usr/bin/python3
"""
List all cities
from the database hbtn_0e_0_usa
"""


from MySQLdb import Connection
import sys


if __name__ == "__main__":
    """
    Connect to a MySQL server
    and list all cities in the database
    using argv and the MySQLdb library
    """
    db = Connection(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name\
            FROM `cities`\
            JOIN `states` \
            ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
