from classes.enemy.enemy import Enemy


class UFO(Enemy):
    def __init__(self, image, pos, size):
        self.speed = 2
        self.damage = 1
        self.health = 10
        self.score = 1
        super().__init__(image, pos, size, self.speed, self.damage, self.health, self.score)