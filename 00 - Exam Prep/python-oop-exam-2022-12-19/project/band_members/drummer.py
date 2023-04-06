from project.band_members.musician import Musician


class Drummer(Musician):
    AVAILABLE_SKILLS = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skills(self, new_skill):
        if new_skill not in Drummer.AVAILABLE_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."


# drummer = Drummer('John', 25)
# print(drummer.__class__.__name__)
# print(drummer.name)
# print(drummer.age)
# print(drummer.learn_new_skills('play the drums with drumsticks'))
# print(drummer.learn_new_skills('sing high pitch notes'))
