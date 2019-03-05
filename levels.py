from obstacle import Obstacle


class Level:
    def __init__(self, obstacles, target, time_limit):
        self.obstacles = obstacles
        self.target = target  # how much food player needs to eat in order to win
        self.time_limit = time_limit


levels = [
    Level([], 5, 60),
    Level([Obstacle(200, 200, 500, 500)], 10, 60),
]
