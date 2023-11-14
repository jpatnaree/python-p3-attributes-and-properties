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
    def __init__(self, name = "name", breed = APPROVED_BREEDS):
        if (type(name) == str) and (1 <= len(name) <= 25):
            self.name = name
        else:
            print('Name must be string between 1 and 25 characters.')
        
        self.breed = breed
        if breed != APPROVED_BREEDS: 
            print('Breed must be in list of approved breeds.')
        
            
        