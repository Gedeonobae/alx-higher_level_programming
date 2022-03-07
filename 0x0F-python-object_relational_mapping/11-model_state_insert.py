#!/usr/bin/python3
"""
    script that adds the State object 'Louisiana' to the database hbtn_0e_6_usa
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
    arg = State(name="Louisiana")
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    session.add(arg)
    session.commit()
    print(arg.id)
    session.close()
