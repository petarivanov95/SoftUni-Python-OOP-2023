from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += 3


# fish = FreshwaterFish("Nemo", "Clownfish", 10.0)
# print(fish.size)
# fish.eat()
# print(fish.size)
# print(fish.price)


