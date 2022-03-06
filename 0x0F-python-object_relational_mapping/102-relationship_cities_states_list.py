#!/usr/bin/python3
"""
    script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    start = sessionmaker()
    start.configure(bind=engine)
    session = start()
    stmt = session.query(City).order_by(City.id)
    for i in stmt:
        print("{:d}: {:s} -> {:s}".format(i.id, i.name, i.state.name))
    session.close()
