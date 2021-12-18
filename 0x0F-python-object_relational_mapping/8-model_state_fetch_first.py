#!/usr/bin/python3

"""
SQLAlchemy Statements

"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

from sqlalchemy import (create_engine)


def connection():
    """Connection to database"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(
                                   argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
    except Exception:
        print("Can't connect to DB")
        return 0

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        for state in session.query(State).all():
            if state.id == 1:
                print("{}: {}".format(state.id, state.name))
    except Exception:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    connection()
