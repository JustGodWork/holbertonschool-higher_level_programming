#!/usr/bin/python3
"""
Module that lists all State objects from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    List all State objects from the database hbtn_0e_6_usa
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(
            argv[1],
            argv[2],
            argv[3]
        )
    )
    session = sessionmaker(bind=engine)()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
