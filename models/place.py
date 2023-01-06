#!/usr/bin/python3
""" Place Module for HBNB project
it inherits from base
"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """A Class place with attributes bellow:
    city_id: city id
    user_id: user id
    name: name input
    description: string of description
    number_rooms: number of room in int
    number_bathrooms: number of bathrooms in int
    max_guest: maximum guest in int
    price_by_night:: pice for a staying in int
    latitude: latitude in flaot
    longitude: longitude in float
    amenity_ids: list of Amenity ids"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenities = [""]

        amenities = relationship("Amenity", secondary="place_amenity", viewonly=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = ""
        number_bathrooms = ""
        max_guest = ""
        price_by_night = ""
        latitude = ""
        longitude = ""
        amenity_ids = ""
