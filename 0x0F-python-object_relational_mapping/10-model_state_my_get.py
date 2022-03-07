#!/usr/bin/python3
"""
    script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    arg = sys.argv[4]
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.query(State).filter_by(
        name=arg).order_by(asc(State.id)).one_or_none()
    if stmt:
        print("{:d}".format(stmt.id))
    else:
        print("Not found")
    session.close()
