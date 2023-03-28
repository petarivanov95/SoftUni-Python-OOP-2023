class Hero:
    def __init__(self, name: str, health: int):
        """
        Constructor for Hero class.
        :param name: The name of the hero.
        :param health: The initial health of the hero.
        """
        self.name = name
        self.health = health

    # def defend(self, damage: int):
    #     self.health -= damage
    #
    #     if self.health <= 0:
    #         self.health = 0
    #
    #         return f"{self.name} was defeated"

    def defend(self, damage):
        if self.health - damage <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        else:
            self.health -= damage

    def heal(self, amount: int) -> None:
        self.health += amount


hero = Hero("Peter", 100) # creates a Hero object named "Peter" with 100 health points
print(hero.defend(50)) # reduces the health of the hero by 50 points and returns None, since the hero is still alive
hero.heal(50) # increases the health of the hero by 50 points
print(hero.defend(99)) # reduces the health of the hero by 99 points and returns a string message indicating that the hero was defeated, since the health is now 1
print(hero.defend(1)) # reduces the health of the hero by 1 point and returns a string message indicating that the hero was defeated, since the health is 

