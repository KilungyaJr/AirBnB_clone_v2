7#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Represents Amenities available to users
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)

    def __init__(self, *args, **kwargs):
        """Init for inherited
        """
        super().__init__(*args, **kwargs)
