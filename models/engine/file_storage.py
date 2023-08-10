#!/usr/bin/python3
'''
this module contains the Filestorage class
that serializes instances to a JSON file and
deserializes JSON file to instances
'''
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    '''
    this is the class FileStorage
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects.
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id.
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file (path: __file_path).
        '''
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        '''
        Deserializes the JSON file to __objects it exists
        '''
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                data = json.load(f)
                for k, v in data.items():
                    cls_value = eval(v["__class__"])(**v)
                    self.__objects[k] = cls_value
        except FileNotFoundError:
            pass
