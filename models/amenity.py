#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True))

class Amenity(BaseModel, Base):
    """
    Represents Amenities available to users
    """
    __tablename__ = "amenities"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity, back_populates="amenities")
    else:
        name = ""
