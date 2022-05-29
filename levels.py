from random import randint
from obstacle import Obstacle
import constants


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
    while len(levels) <= level:
        obstacles = []
        while len(obstacles) < level:
            w = randint(0, 100)
            h = randint(0, 100)
            x = randint(0, constants.WIDTH - w)
            y = randint(0, constants.HEIGHT - h)
            if max(x, y) < 100:
                continue
            obstacles.append(Obstacle(x, y, w, h))
        levels.append(Level(obstacles, 9, 60))