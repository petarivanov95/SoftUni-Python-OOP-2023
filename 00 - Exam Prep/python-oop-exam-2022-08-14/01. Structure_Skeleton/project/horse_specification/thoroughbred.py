from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TRAIN_SPEED = 3

    def train(self):
        self.speed += self.TRAIN_SPEED
