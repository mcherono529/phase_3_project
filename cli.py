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

def list_animals():
    animals = session.query(Animal).all()
    if not animals:
        print("No animals found.")
        return
    for animal in animals:
        print(animal)

def update_animal():
    list_animals()
    animal_id = int(input("Enter the ID of the animal to update: "))
    animal = session.get(Animal, animal_id)

    if not animal:
        print("Animal not found. Please try again.")
        return

    animal.name = input(f"Enter new name (current: {animal.name}): ") or animal.name
    animal.species = input(f"Enter new species (current: {animal.species}): ") or animal.species
    animal.age = int(input(f"Enter new age (current: {animal.age}): ") or animal.age)
    list_habitats()
    new_habitat_id = input(f"Enter new habitat ID (current: {animal.habitat_id}): ") or animal.habitat_id

    new_habitat = session.get(Habitat, int(new_habitat_id)) if new_habitat_id else None
    if new_habitat_id and not new_habitat:
        print("Invalid habitat ID. Update canceled.")
        return

    animal.habitat_id = new_habitat_id
    session.commit()
    print(f"Animal '{animal.name}' updated successfully.")

