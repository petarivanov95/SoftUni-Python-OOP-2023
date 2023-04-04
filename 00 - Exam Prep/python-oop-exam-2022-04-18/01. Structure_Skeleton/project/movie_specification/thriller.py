class Thriller(Movie):
    default_age_restriction = 16

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = None):
        super().__init__(title, year, owner, age_restriction or self.default_age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value is not None and value < self.default_age_restriction:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
