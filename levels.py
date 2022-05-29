from random import randint
from obstacle import Obstacle
import constants


class Level:
    def __init__(self, obstacles, target, time_limit):
        self.obstacles = obstacles
        self.target = target  # how much food player needs to eat in order to win
        self.time_limit = time_limit

def add_borders(obstacles):
    bs = 2
    off = -bs // 2
    obstacles.append(Obstacle(0, off, constants.WIDTH, bs))
    obstacles.append(Obstacle(0, constants.HEIGHT + off, constants.WIDTH, bs))
    obstacles.append(Obstacle(off, 0, bs, constants.HEIGHT))
    obstacles.append(Obstacle(constants.WIDTH + off, 0, bs, constants.HEIGHT))
    return obstacles

levels = [
    Level(add_borders([]), 5, 60),
    Level(add_borders([Obstacle(200, 200, 500, 500)]), 10, 60),
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
        levels.append(Level(add_borders(obstacles), 9, 60))