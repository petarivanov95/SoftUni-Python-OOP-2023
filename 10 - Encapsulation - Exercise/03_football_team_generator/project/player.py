class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Player: {self.__name}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}"


# p = Player("Pall", 1, 3, 5, 7)
#
# print("Player name:", p.name)
# print("Points sprint:", p._Player__sprint)
# print("Points dribble:", p._Player__dribble)
# print("Points passing:", p._Player__passing)
# print("Points shooting:", p._Player__shooting)
#
# print("\ncalling the __str__ method")
# print(p)
