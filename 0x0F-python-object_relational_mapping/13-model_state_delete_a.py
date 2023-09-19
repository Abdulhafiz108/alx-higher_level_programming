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

    states = my_session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        my_session.delete(state)

    my_session.commit()

    my_session.close()
