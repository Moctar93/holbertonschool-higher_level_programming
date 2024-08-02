#!/usr/bin/python3
"""Fetch and display all City objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./14-model_city_fetch_by_state.py <username> <password> <database>")
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
    
    # Query to get all City objects with their associated State objects
    cities = session.query(City, State).join(State).order_by(City.id).all()
    
    # Print the results in the specified format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    
    # Close the session
    session.close()

