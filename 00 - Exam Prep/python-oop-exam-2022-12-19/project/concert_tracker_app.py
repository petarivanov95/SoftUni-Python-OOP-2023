from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN = {
        'Guitarist':Guitarist,
        'Drummer': Drummer,
        'Singer': Singer
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN:
            raise ValueError("Invalid musician type!")
        musician_names = [x.name for x in self.musicians]
        if name in musician_names:
            raise Exception(f"{name} is already a musician!")
        new_musician = self.VALID_MUSICIAN[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{new_musician.name} is now a {musician_type}."

    def create_band(self, name):
        band_names = [x.name for x in self.bands]
        if name in band_names:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{new_band.name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concerts_with_same_name = [x for x in self.concerts if x.place == place]
        if len(concerts_with_same_name) > 0:
            raise Exception(f"{place} is already registered for {concerts_with_same_name[0].genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{new_concert.genre} concert in {new_concert.place} was added."

    def add_musician_to_band(self, musician_name, band_name):
        musician_names = [x.name for x in self.musicians]
        if musician_name not in musician_names:
            raise Exception(f"{musician_name} isn't a musician!")



musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))
#
print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
# for i in range(3):
#     print(app.add_musician_to_band(names[i], "RockName"))
#
print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
#
# print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
# print(app.start_concert("Sofia", "RockName"))
