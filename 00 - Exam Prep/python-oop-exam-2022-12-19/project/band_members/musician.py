from abc import ABC, abstractmethod


class Musician(ABC):



    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = [] # TODO A musician CANNOT learn a skill that is NOT in the list of available types (see below).

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value.isspace():
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self.__age = value

    @abstractmethod
    def learn_new_skills(self, new_skill):
        ...