#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    This class defines a user by various attributes with their information
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="delete", backref="user")
    reviews = relationship("Review", cascade="delete", backref="user")

    def __init__(self, *args, **kwargs):
        """
        inherit from base  and Basemodel init
        """
        super().__init__(*args, **kwargs)
