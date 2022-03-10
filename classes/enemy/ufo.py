from classes.enemy.enemy import Enemy


class UFO(Enemy):
    def __init__(self, image, pos, size):
        self._speed = 2
        self._damage = 1
        self._health = 10
        self._score = 1
        super().__init__(image, pos, size, self._speed, self._damage, self._health, self._score)
