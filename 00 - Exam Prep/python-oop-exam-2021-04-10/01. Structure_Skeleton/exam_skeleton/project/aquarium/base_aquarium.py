from abc import ABC,abstractmethod

from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    possible_fish_types = {
        'FreshwaterFish':FreshwaterFish,
        'SaltwaterFish':SaltwaterFish
                           }

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isspace():
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([x.comfort for x in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        if fish.__class__.__name__ in BaseAquarium.possible_fish_types:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for x in self.fish:
            x.eat()

    def __str__(self):
        def __str__(self):
            fish_names = " ".join([f.name for f in self.fish]) if self.fish else "none"
            return f"{self.name}:\nFish: {fish_names}\nDecorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"

