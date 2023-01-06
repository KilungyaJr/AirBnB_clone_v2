#!/usr/bin/python3
"""
Review module for the HBNB project
it inherits from BaseModel and Base
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    """
    Review class to store review information of users
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """Init for inherited
        """
        super().__init__(*args, **kwargs)
