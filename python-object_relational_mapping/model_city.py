#!/usr/bin/python3
"""
Module that contains the class definition of a City.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
        Class City that inherits from Base
        Attributes:
            id (int): id of the city
            name (str): name of the city
            state_id (int): id of the state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
