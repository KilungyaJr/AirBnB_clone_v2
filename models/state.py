#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns the list of `City` instances
            with `state_id` equals to the current
            """
            cities = []

            for city in models.storage.all(City):
                if city.state_id == self.id:
                    cities.append(city)
            return cities
