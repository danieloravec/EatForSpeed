from random import randint

import constants as C

class Food:
    def __init__(self):
        # TODO avoid generating food inside a player
        self.x = randint(100, C.WIDTH - 100)
        self.y = randint(100, C.HEIGHT - 100)
        self.side = 10
        self.color = (255, 0, 0)
