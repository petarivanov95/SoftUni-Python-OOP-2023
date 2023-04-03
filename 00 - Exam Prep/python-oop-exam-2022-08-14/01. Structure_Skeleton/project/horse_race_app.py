from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def get_jockey(self, name):
        try:
            jockey = [j for j in self.jockeys if j.name == name][0]
        except IndexError:
            raise Exception(f"Jockey {name} could not be found!")
        return jockey

    def get_race(self, race_type):
        try:
            race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")
        return race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse_names = [x.name for x in self.horses]
        if horse_type in self.VALID_HORSE_TYPES:
            if horse_name in horse_names:
                raise Exception(f"Horse {horse_name} has been already added!")

            new_horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey_names = [x.name for x in self.jockeys]
        if jockey_name in jockey_names:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        created_race_types = [x.race_type for x in self.horse_races]
        if race_type in created_race_types:
            raise Exception("Race {race type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.get_jockey(jockey_name)
        jockey_names = [x.name for x in self.jockeys]
        # available_horse_types = [x.race_type for x in self.horses if x.is_taken is False]

        if jockey.name not in jockey_names:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for horse in self.horses[::-1]:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                if jockey.horse is not None:
                    return f"Jockey {jockey_name} already has a horse."

                jockey.horse = horse
                horse.is_taken = True
                return f"Jockey {jockey_name} will ride the horse {horse.name}."
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.get_jockey(jockey_name)
        race = self.get_race(race_type)

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for race_jockey in race.jockeys:
            if race_jockey.name == jockey.name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        if jockey.horse is not None:
            race.jockeys.append(jockey)
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.get_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        top_jockey = ""
        top_horse = ""
        top_horse_speed = 0
        for jockey in race.jockeys:
            if jockey.horse.speed > top_horse_speed:
                top_jockey = jockey.name
                top_horse = jockey.horse.name
                top_horse_speed = jockey.horse.speed

        return f"The winner of the {race_type} race, with a speed of {top_horse_speed}km/h" \
               f" is {top_jockey}! Winner's horse: {top_horse}."


# horseRaceApp = HorseRaceApp()
# print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
# print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.start_horse_race("Summer"))
