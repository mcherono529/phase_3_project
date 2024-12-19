from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import sys

Base = declarative_base()

class Habitat(Base):
    __tablename__ = "habitats"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    animals = relationship("Animal", back_populates="habitat")

    def __repr__(self):
        return f"Habitat(id={self.id}, name='{self.name}', type='{self.type}')"


class Animal(Base):
    __tablename__ = "animals"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    habitat_id = Column(Integer, ForeignKey("habitats.id"))

    habitat = relationship("Habitat", back_populates="animals")

    def __repr__(self):
        return f"Animal(id={self.id}, name='{self.name}', species='{self.species}', age={self.age}, habitat_id={self.habitat_id})"
