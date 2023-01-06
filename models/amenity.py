#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String


class Amenity(BaseModel):
    """
    Represents Amenities available to users
    """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
