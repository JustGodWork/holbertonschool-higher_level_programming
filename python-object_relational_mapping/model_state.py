#!/usr/bin/python3
"""
Module that contains the class definition of a State
and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
        Class State that inherits from Base
        Attributes:
            id (int): id of the state
            name (str): name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
