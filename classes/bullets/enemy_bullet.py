from classes.bullets.bullet import Bullet


class EnemyBullet(Bullet):
    def __init__(self, image, pos, rotate_coef, size, damage):
        self._size = size
        self._speed = 5
        self._damage = damage
        super().__init__(image, pos, rotate_coef, self._size, self._speed, self._damage)
