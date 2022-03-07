#!/usr/bin/python3
"""
    script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
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
        arg = argv[4]
        stmt = """
        SELECT cities.name
        FROM cities
        WHERE cities.state_id LIKE BINARY
        (SELECT states.id FROM states WHERE states.name LIKE BINARY %s)
        ORDER BY cities.id ASC
        """
        cur.execute(stmt, (arg,))
        rtn = cur.fetchall()
    except MySQLdb.Error:
        try:
            rtn = ("MySQLdb Error")
        except IndexError:
            rtn = ("MySQLdb Error - IndexError")
    rslt = []
    for i in rtn:
        rslt += i
    print(", ".join(rslt))
    cur.close()
    conn.close()
