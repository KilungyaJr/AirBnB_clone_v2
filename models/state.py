#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            backref="state",
            cascade="all,
            delete-orphan")

    def __init__(self, *args, **kwargs):
        """init inherited
        """
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns the list of `City` instances
            with `state_id` equals to the current
            """
            cities = []

            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
