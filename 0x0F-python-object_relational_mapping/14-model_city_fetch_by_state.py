#!/usr/bin/python3

"""
SQLAlchemy Statements

"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
    for state, city in session.query(State, City).\
            filter(City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    connection()
