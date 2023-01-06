#!/usr/bin/python3
""" Place Module for HBNB project
it inherits from base
"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
import models
from models.amenity import Amenity, place_amenity
from models.review import Review


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

    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") == "db":
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
        amenity_ids = []

        reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

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

    @property
    def reviews(self):
        """Get a list of all linked Reviews.
        """
        review_list = []

        for review in models.storage.all(Review).values():
            if review.place_id == self.id:
                review_list.append(review)

        return review_list

    @property
    def amenities(self):
        amenities = []
        for amenity_id in self.amenity_ids:
            amenity = models.storage.get(Amenity, amenity_id)
            if amenity is not None:
                amenities.append(amenity)
        return amenities

    @amenities.setter
    def amenities(self, amenity):
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
