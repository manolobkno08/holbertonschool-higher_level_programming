#!/usr/bin/python3

"""
Class definition of State

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

from relationship_state import Base


class City(Base):
    """ City table """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
