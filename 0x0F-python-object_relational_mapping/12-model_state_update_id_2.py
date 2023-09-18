#!/usr/bin/python3
"""Changes name of State object in a database
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

    state = my_session.query(State).filter_by(id = 2).first()
    state.name = "New Mexico"
    my_session.commit()

    my_session.close()
