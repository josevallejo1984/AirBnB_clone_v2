#!/usr/bin/python3
"""State Module for HBNB project."""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """State class."""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            """Return list of Cities with the current state_id."""
            list_cities = []

            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    list_cities.append(city)

            return list_cities
