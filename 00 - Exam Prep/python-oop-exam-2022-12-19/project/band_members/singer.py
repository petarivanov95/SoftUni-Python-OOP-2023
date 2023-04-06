from project.band_members.musician import Musician


class Singer(Musician):
    AVAILABLE_SKILLS = ["sing high pitch notes", "sing low pitch notes"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skills(self, new_skill):
        if new_skill not in Singer.AVAILABLE_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."


# singer = Singer('John', 25)
# print(singer.name)
# print(singer.age)
# print(singer.learn_new_skills('sing high pitch notes'))
# print(singer.learn_new_skills('sing high pitch notes'))
