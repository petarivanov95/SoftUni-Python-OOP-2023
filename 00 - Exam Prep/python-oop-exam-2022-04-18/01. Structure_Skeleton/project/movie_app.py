from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False


    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        owner = movie.owner
        if owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if owner not in self.users_collection:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        owner.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie, **kwargs):
        if not self.check_if_movie_exists(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            for attr, new_value in kwargs.items():
                setattr(movie, attr, new_value)
            return f'{username} successfully edited {movie.title} movie.'


movie_app = MovieApp()
print(movie_app.register_user('Martin', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Martin', movie))
print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))
user2 = movie_app.users_collection[1]
movie2 = Action('Free Guy', 2021, user2, 16)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.like_movie('Alexandra', movie))
# print(movie_app.dislike_movie('Martin', movie2))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.delete_movie('Alexandra', movie2))
# movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.display_movies())
# print(movie_app)
