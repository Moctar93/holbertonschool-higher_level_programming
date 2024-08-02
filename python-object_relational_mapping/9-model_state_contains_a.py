#!/usr/bin/python3
"""List all State objects that contain the letter 'a' from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_contains_a.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine and connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()
    
    # Query State objects containing 'a', ordered by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()

