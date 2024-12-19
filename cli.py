import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Habitat,Animal

DATABASE_URL = "sqlite:///habitats.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print("Database Initialized")

def add_habitat():
    name = input("Enter habitat name: ")
    type_ = input("Enter habitat type: ")
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

def remove_animal():
    list_animals()
    animal_id = int(input("Enter the ID of the animal to remove: "))
    animal = session.get(Animal, animal_id)
 
    if not animal:
        print("Animal not found. Please try again.")
        return

    session.delete(animal)
    session.commit()
    print(f"Animal '{animal.name}' removed successfully.")

def view_habitat_animals():
    list_habitats()
    habitat_id = int(input("Enter the ID of the habitat to view its animals: "))
    habitat = session.get(Habitat, habitat_id)

    if not habitat:
        print("Habitat not found. Please try again.")
        return

    animals_in_habitat = habitat.animals

    if not animals_in_habitat:
        print(f"No animals found in habitat '{habitat.name}'.")
        return

    print(f"Animals in habitat '{habitat.name}':")
    for animal in animals_in_habitat:
        print(animal)

def main_menu():
    while True:
        print("\nAnimal Zoo Management CLI App")
        print("1. Add Habitat")
        print("2. List Habitats")
        print("3. Add Animal")
        print("4. List Animals")
        print("5. Update Animal")
        print("6. Remove Animal")
        print("7. View Animals in a Habitat")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_habitat()
        elif choice == "2":
            list_habitats()
        elif choice == "3":
            add_animal()
        elif choice == "4":
            list_animals()
        elif choice == "5":
            update_animal()
        elif choice == "6":
            remove_animal()
        elif choice == "7":
            view_habitat_animals()
        elif choice == "8":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    init_db()
    main_menu()
