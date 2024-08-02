#!/usr/bin/python3
"""Delete all State objects with a name containing the letter 'a'"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./13-model_state_delete_a.py <username> <password> <database>")
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
    
    # Query for all states with a name containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    
    # Delete the states
    for state in states_to_delete:
        session.delete(state)
    
    # Commit the transaction
    session.commit()
    
    # Close the session
    session.close()

