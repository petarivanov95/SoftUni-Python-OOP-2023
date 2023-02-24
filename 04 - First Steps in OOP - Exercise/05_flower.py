class Flower:
    def __init__(self, name: str, water_requirements: int):
        # Constructor method that initializes the Flower object with a name and water requirements.
        # Also sets the is_happy attribute to False by default.
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int) -> None:
        # Method that waters the flower with a specified quantity of water.
        # If the quantity is greater than or equal to the water requirements,
        # the is_happy attribute is set to True, indicating that the flower is happy.
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        # Method that returns a string indicating whether the flower is happy or not.
        # If the is_happy attribute is True, the flower is happy, otherwise it's not happy.
        return f"{self.name} is {'' if self.is_happy else 'not '}happy"

        # Alternatively, the above line could be replaced with the following code:
        # if self.is_happy:
        #     return f"{self.name} is happy"
        # else:
        #     return f"{self.name} is not happy"


# Example usage:
flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())  # Output: Lilly is not happy
flower.water(60)
print(flower.status())  # Output: Lilly is not happy
flower.water(100)
print(flower.status())  # Output: Lilly is happy
