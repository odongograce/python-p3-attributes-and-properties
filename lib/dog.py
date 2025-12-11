#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self.name=name
        self.breed =breed
    def set_name(self, name):
        if (type(name) in (str)) and (1 <= name <= 25):
            print(f"Setting name to { name }.")
            self._name = name

        else:
            print("Name must be string between 1 and 25 characters.")
    # def set_breed(self, breed):
        
   