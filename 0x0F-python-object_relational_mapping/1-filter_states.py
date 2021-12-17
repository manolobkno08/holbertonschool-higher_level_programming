#!/usr/bin/python3

import MySQLdb
from sys import argv

conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
