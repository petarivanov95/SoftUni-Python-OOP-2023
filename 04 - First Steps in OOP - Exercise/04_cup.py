class Cup:
    def __init__(self, size: int, quantity: int):
        """
        Constructor for Cup class.
        :param size: The maximum capacity of the cup in milliliters.
        :param quantity: The current quantity of liquid in the cup in milliliters.
        """
        self.size = size
        self.quantity = quantity

    def fill(self, quantity: int) -> None:
        """
        Fills the cup with a given quantity of liquid if it doesn't exceed the maximum capacity.
        :param quantity: The quantity of liquid to add to the cup in milliliters.
        """
        if self.quantity + quantity <= self.size:
            self.quantity += quantity

    def status(self) -> int:
        """
        Returns the remaining space in the cup in milliliters.
        :return: The remaining space in the cup in milliliters.
        """
        return self.size - self.quantity


cup = Cup(100, 50) # creates a Cup object with a maximum capacity of 100 ml and 50 ml of liquid in it
print(cup.status()) # prints the remaining space in the cup, which is 50 ml
cup.fill(40) # adds 40 ml of liquid to the cup
cup.fill(20) # adds 20 ml of liquid to the cup
print(cup.status()) # prints the remaining space in the cup, which is now 10 ml
