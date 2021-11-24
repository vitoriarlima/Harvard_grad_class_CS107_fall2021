#!/usr/bin/python3


class Animal:
    
    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    
    def __init__(self, name, species):
        self.name = name
        self._species = species


    def __repr__(self):
        return f'{self.name} ({self._species})'
    
    @property
    def species(self):
        return self._species
    
    ##Add another method species(self, into) to the Animal class. 
    ##This method should set the _species attribute of this Animal to into, 
    ##but before that, it makes sure that into is in the valid_species 
    ##list. If into is not in the valid_species list, raise an Exception. 
    ##Apply the species.setter decorator to this method.
    
    @species.setter
    def species(self, into):
        assert into in Animal.valid_species, Exception(f'invalid species: {into}')
        self._species = into


>>> dog = Animal('Fido', 'dog')
>>> vars(dog)

>>> dog = Animal('Fido', 'dog')
>>> dog.species

>>> dog.species = 'cat'
>>> dog.species

>>> dog.species = 'TheThing'

