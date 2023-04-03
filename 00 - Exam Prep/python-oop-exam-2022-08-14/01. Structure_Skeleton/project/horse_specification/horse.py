from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_SPEED = None

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False # TODO KEEP IN MIND ONLY ONE HORSE WITH ONE RIDER

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @staticmethod
    @abstractmethod
    def maximum_speed():
        pass

    @staticmethod
    @abstractmethod
    def train_speed():
        pass

    def train(self):
        if self.speed + self.train_speed() > self.maximum_speed():
            self.speed = self.maximum_speed()
        else:
            self.speed += self.train_speed()