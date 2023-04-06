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
        musician = [x for x in self.musicians if x.name == musician_name][0]
        band_names = [x.name for x in self.bands]
        band = [x for x in self.bands if x.name == band_name][0]
        if musician_name not in musician_names:
            raise Exception(f"{musician_name} isn't a musician!")
        if band_name not in band_names:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name, band_name):
        band_names = [x.name for x in self.bands]
        band = [x for x in self.bands if x.name == band_name][0]
        musician_names_in_band = [x.name for x in band.members]
        musician = [x for x in band.members if x.name == musician_name][0]
        if band_name not in band_names:
            raise Exception(f"{band_name} isn't a band!")
        if musician_name not in musician_names_in_band:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        band = next(filter(lambda b: b.name == band_name, self.bands))
        types_of_musicians_in_band = {x.__class__.__name__ for x in band.members}

        if len(types_of_musicians_in_band) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        error_message = f"The {band_name} band is not ready to play at the concert!"

        if concert.genre == "Rock":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Singer" and "sing high pitch notes" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Guitarist" and "play rock" not in member.skills:
                    raise Exception(error_message)

        elif concert.genre == "Metal":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Singer" and "sing low pitch notes" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Guitarist" and "play metal" not in member.skills:
                    raise Exception(error_message)

        elif concert.genre == 'Jazz':
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drum brushes" not in member.skills:
                    raise Exception(error_message)
                elif member.__class__.__name__ == "Singer":
                    if "sing low pitch notes" not in member.skills or "sing high pitch notes" not in member.skills:
                        raise Exception(error_message)
                elif member.__class__.__name__ == "Guitarist" and "play jazz" not in member.skills:
                    raise Exception(error_message)

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."


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
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

# print(app.remove_musician_from_band('Lilly',"RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
#
# print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))
