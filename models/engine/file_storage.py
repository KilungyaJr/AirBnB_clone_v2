#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns the list of objects of one type of class"""
        if cls:
            sameType = dict()

            for key, obj in self.__objects.items():
                if obj.__class__ == cls:
                    sameType[key] = obj
            return sameType

        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes obj from __objects if it’s inside
        if obj is equal to None, the method should not do anything
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)

            if self.__objects[key]:
                del self.__objects[key]
                self.save()

    def close(self):
        """Deserialize the JSON file to objects
        """
        self.reload()
