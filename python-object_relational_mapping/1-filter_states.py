#!/usr/bin/python3
"""
Select all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

from MySQLdb import Connection
import sys

if __name__ == "__main__":
    """
    Connect to a MySQL server
    and list all states with a name
    starting with N (upper N) in the database
    using argv and the MySQLdb library
    """
    db = Connection(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT `id`, `name` FROM `states` \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY `id` ASC"
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
