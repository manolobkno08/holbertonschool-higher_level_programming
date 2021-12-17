#!/usr/bin/python3

import MySQLdb
from sys import argv

conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name = '{name}' ORDER BY id ASC"
            .format(name=argv[4]))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
