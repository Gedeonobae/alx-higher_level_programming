#!/usr/bin/python3
""" write one script that is safe from MySQL injections! """
from sys import argv
import MySQLdb
if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")
    cur = conn.cursor()
    try:
        search = argv[4]
        stmt = """
        SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC
        """
        cur.execute(stmt, (search,))
        rtn = cur.fetchall()
    except MySQLdb.Error:
        try:
            rtn = ("MySQLdb Error")
        except IndexError:
            rtn = ("MySQLdb Error - IndexError")
    for i in rtn:
        print(i)
    cur.close()
    conn.close()
