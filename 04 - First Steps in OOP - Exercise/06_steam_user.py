from typing import List

class SteamUser:
    def __init__(self, username: str, games: List[str]):
        # Constructor method that initializes the SteamUser object with a username and a list of games.
        # Also sets the played_hours attribute to 0 by default.
        self.username = username
        self.games = games  # ["The crew", "The crew 2", "NFS"]
        self.played_hours = 0

    def play(self, game: str, hours: int) -> str:
        # Method that allows the user to play a game for a certain number of hours.
        # If the game is in the user's library, the played_hours attribute is updated
        # and a message is returned indicating the user is playing the game.
        # If the game is not in the user's library, a message is returned indicating the game is not in the library.
        if game in self.games:
            self.played_hours += hours

            return f"{self.username} is playing {game}"

        return f"{game} is not in library"

    def buy_game(self, game: str) -> str:
        # Method that allows the user to buy a game and add it to their library.
        # If the game is not already in the user's library, it is added
        # and a message is returned indicating the user has bought the game.
        # If the game is already in the user's library, a message is returned indicating the game is already in the library.
        if game not in self.games:
            self.games.append(game)

            return f"{self.username} bought {game}"

        return f"{game} is already in your library"

    def status(self) -> str:
        # Method that returns a string indicating the user's username, the number of games in their library,
        # and the total play time across all games.
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


# Example usage:
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))  # Output: Peter is playing Fortnite
print(user.play("Oxygen Not Included", 5))  # Output: Oxygen Not Included is not in library
print(user.buy_game("CS:GO"))  # Output: CS:GO is already in your library
print(user.buy_game("Oxygen Not Included")) 
