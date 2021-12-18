#!/usr/bin/python3

import MySQLdb
from sys import argv


def connection():
    """
    Simple Query Function
    """
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3], charset="utf8")
    except Exception:
        print("Can't connect to DB")
        return 0
    cur = conn.cursor()
    cur.execute(
        """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = '{state}'
        ORDER BY cities.state_id ASC
        """.format(state=argv[4])
    )

    query_rows = cur.fetchall()
    print(", ".join(city[0] for city in query_rows))

    cur.close()
    conn.close()


connection()
