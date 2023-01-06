#!/usr/bin/python3
"""Defines the DBStorage engine"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Defines the DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """creates the __engine attribute, which is linked to the MySQL database
        specified by the environment variables
        """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        dialect = 'mysql'
        driver = 'mysqldb'
        self.__engine = create_engine(f"{dialect}://{user}:{pwd}@{host}/{db}", pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """queries the current database session for all objects of a given class
        (or all classes if no class is specified),
        and returns a dictionary with the objects
        """
        result = {}
        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f'{cls.__name__}.{obj.id}'
                result[key] = obj
        else:
            for cls in BaseModel.__subclasses__():
                objects = self.__session.query(cls).all()
                for obj in objects:
                    key = f'{cls.__name__}.{obj.id}'
                    result[key] = obj
        return result

    def new(self, obj):
        """add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
        self.__session.commit()

    def reload(self):
        """creates all the tables in the database and creates the
        current database session using a sessionmaker and a scoped_session.
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Closes and stops the session"""
        self.__session.close()
