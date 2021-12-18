#!/usr/bin/python3

"""
Class definition of State

"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class City(Base):
    """ City table """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
