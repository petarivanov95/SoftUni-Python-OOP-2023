from project.band_members.musician import Musician


class Guitarist(Musician):
    AVAILABLE_SKILLS = ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill):
        if new_skill not in Guitarist.AVAILABLE_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."


# guitarist = Guitarist('John', 25)
# print(guitarist.__class__.__name__)
# print(guitarist.name)
# print(guitarist.age)
# print(guitarist.learn_new_skills('play metal'))
# print(guitarist.learn_new_skills('sing high pitch notes'))
