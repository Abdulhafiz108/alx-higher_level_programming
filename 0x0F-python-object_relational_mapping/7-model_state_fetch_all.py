#!/usr/bin/python3
"""lists all State objects from a database
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

    for state in my_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    my_session.close()
