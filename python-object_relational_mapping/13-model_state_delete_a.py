#!/usr/bin/python3
"""
Module that deletes all State objects
with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Delete all State objects with a name containing the letter 'a'
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
        session.delete(state)
    session.commit()
    session.close()
