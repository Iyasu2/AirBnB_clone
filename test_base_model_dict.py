#!/usr/bin/python3
"""
Test script to check BaseModel class behavior
"""

from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                   my_model_json[key]))

# Recreate instance from dictionary
my_new_model = BaseModel.from_dict(my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
print(my_model is my_new_model)