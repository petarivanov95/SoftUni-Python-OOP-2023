from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    def __init__(self, name: str, species: str,  price: float):
        super().__init__(name, species, 5, price)

    def eat(self):
        self.size += 2


# fish = SaltwaterFish("Nemo", "Clownfish", 8)
# print(fish.size)
# fish.eat()
# print(fish.size)
# print(fish.price)

