#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker

from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")
    session.close()
