#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""
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
        SELECT * FROM states WHERE name LIKE BINARY '{:s}' ORDER BY id ASC;
        """.format(search)
        cur.execute(stmt)
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
