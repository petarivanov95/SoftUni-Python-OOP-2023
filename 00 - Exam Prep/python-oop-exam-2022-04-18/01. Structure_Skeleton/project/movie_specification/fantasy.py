from project.movie_specification.movie import Movie
from project.user import User


class Fantasy(Movie):
    default_age_restriction = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = None):
        super().__init__(title, year, owner, age_restriction or self.default_age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.default_age_restriction:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

# test_user = User('John',3)
# movie = Fantasy('Hero',2000,test_user,16)
# print(movie.details())