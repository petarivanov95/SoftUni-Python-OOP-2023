class Hero:
    def __init__(self, name: str, health: int):
        """
        Constructor for Hero class.
        :param name: The name of the hero.
        :param health: The initial health of the hero.
        """
        self.name = name
        self.health = health

    def defend(self, damage: int):
        """
        Decreases the health of the hero by a given amount of damage.
        :param damage: The amount of damage to be inflicted on the hero.
        :return: A string message indicating that the hero was defeated, or None if the hero is still alive.
        """
        self.health -= damage

        if self.health <= 0:
            self.health = 0

            return f"{self.name} was defeated"

    def heal(self, amount: int) -> None:
        """
        Increases the health of the hero by a given amount.
        :param amount: The amount to be added to the hero's health.
        """
        self.health += amount


hero = Hero("Peter", 100) # creates a Hero object named "Peter" with 100 health points
print(hero.defend(50)) # reduces the health of the hero by 50 points and returns None, since the hero is still alive
hero.heal(50) # increases the health of the hero by 50 points
print(hero.defend(99)) # reduces the health of the hero by 99 points and returns a string message indicating that the hero was defeated, since the health is now 1
print(hero.defend(1)) # reduces the health of the hero by 1 point and returns a string message indicating that the hero was defeated, since the health is 
