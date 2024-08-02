#!/usr/bin/python3
"""Update the name of a State object in the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./12-model_state_update.py <username> <password> <database>")
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
    
    # Query for the state with id = 2
    state = session.query(State).filter_by(id=2).first()
    
    # Update the state name if it exists
    if state:
        state.name = "New Mexico"
        session.commit()
    
    # Close the session
    session.close()

