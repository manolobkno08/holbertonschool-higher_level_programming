#!/usr/bin/python3

"""
SQLAlchemy Statements

"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    res = session.query(State).join(City).order_by(
        State.id, City.id).filter(City.state_id == State.id).all()
    for s in res:
        print(f'{s.id}: {s.name}')
        for c in s.cities:
            print(f'    {c.id}: {c.name}')
    session.close()


if __name__ == "__main__":
    connection()
