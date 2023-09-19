#!/usr/bin/python3
"""Deletes all State object with letter a in a database
"""
from sqlalchemy import (create_engine)
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )

    session_maker = sessionmaker(bind=engine)
    my_session = session_maker()

    cities = my_session.query(City, State).filter(State.id == City.state_id).all()
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    my_session.close()
