from obstacle import Obstacle
import constants as C
from random import randint


class Level:
    def __init__(self, obstacles, target, time_limit):
        self.obstacles = obstacles
        self.target = target  # how much food player needs to eat in order to win
        self.time_limit = time_limit


levels = [
    Level([], 5, 60),
    Level([Obstacle(200, 200, 500, 500)], 10, 60),
]


def generate_level(level):
    if len(levels) > level:
        return

    obstacles = []
    for i in range(level):
        top = randint(0, C.HEIGHT)
        left = randint(0, C.WIDTH)
        w = randint(0, 200)
        h = randint(0, 200)
        obstacles.append(Obstacle(left, top, w, h))

    levels.append(Level(obstacles, 9, 60))
