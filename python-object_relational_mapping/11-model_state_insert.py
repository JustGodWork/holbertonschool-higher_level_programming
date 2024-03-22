#!/usr/bin/python3
"""
Module that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Add the State object “Louisiana” to the database hbtn_0e_6_usa
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
    louisiana = State(name='Louisiana')
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
    session.close()
