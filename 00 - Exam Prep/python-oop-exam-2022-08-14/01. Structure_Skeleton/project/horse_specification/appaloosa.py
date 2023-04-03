from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAIN_SPEED = 3

    def train(self):
        self.speed += self.TRAIN_SPEED
