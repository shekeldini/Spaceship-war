from classes.bullets.bullet import Bullet


class PlayerBullet(Bullet):
    def __init__(self, image, pos, rotate_coef, size):
        self._size = size
        self._speed = 10
        self._damage = 2
        super().__init__(image, pos, rotate_coef, self._size, self._speed, self._damage)