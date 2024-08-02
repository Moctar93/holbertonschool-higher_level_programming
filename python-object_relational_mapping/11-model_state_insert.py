#!/usr/bin/python3
"""Add a new State object “Louisiana” to the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./11-model_state_insert.py <username> <password> <database>")
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
    
    # Create a new State object
    new_state = State(name="Louisiana")
    
    # Add the new State object to the session
    session.add(new_state)
    
    # Commit the session to persist the changes
    session.commit()
    
    # Print the id of the newly created state
    print(new_state.id)
    
    # Close the session
    session.close()

