import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Habitat,Animal

DATABASE_URL = "sqlite:///habitats.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# CLI functionality
def init_db():
    Base.metadata.create_all(engine)
    print("Database Initialized")

def add_habitat():
    name = input("Enter habitat name: ")
    type_ = input("Enter habitat type (e.g., Savannah, Aquarium): ")
    habitat = Habitat(name=name, type=type_)
    session.add(habitat)
    session.commit()
    print(f"Habitat '{name}' added successfully.")

