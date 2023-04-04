class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.isspace():
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        liked_movies_str = "\n".join([str(movie) for movie in self.movies_liked]) or "No movies liked."
        owned_movies_str = "\n".join([str(movie) for movie in self.movies_owned]) or "No movies owned."
        return f"Username: {self.username}, Age: {self.age}\nLiked movies:\n{liked_movies_str}\nOwned movies:\n{owned_movies_str}"


# test_user = User('John',20)
# test_user.movies_liked = ['1','2','3']
# test_user.movies_owned = ['4','5','6']
#
# print(test_user)