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

def list_habitats():
    habitats = session.query(Habitat).all()
    if not habitats:
        print("No habitats found.")
        return
    for habitat in habitats:
        print(habitat)

def add_animal():
    name = input("Enter animal name: ")
    species = input("Enter species: ")
    age = int(input("Enter age: "))
    list_habitats()
    habitat_id = int(input("Enter the ID of the habitat to assign this animal: "))

    habitat = session.get(Habitat, habitat_id)
    if not habitat:
        print("Invalid habitat ID. Please try again.")
        return

    animal = Animal(name=name, species=species, age=age, habitat_id=habitat_id)
    session.add(animal)
    session.commit()
    print(f"Animal '{name}' added successfully.")

