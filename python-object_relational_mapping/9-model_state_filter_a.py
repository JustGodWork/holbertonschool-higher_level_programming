#!/usr/bin/python3
"""
Module that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    List all State objects that contain the letter a
    from the database hbtn_0e_6_usa
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
    query = session.query(State)
    for state in query.filter(State.name.contains('a')):
        print("{}: {}".format(state.id, state.name))
    session.close()
