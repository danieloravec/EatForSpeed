class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.side = 50
        self.step = 1
        self.dx = (0, 1, 1, 1, 0, -1, -1, -1)
        self.dy = (-1, -1, 0, 1, 1, 1, 0, -1)
        self.color = (0, 255, 0)
        self.score = 0

    def move(self, direction):
        self.x += self.dx[direction] * self.step
        self.y += self.dy[direction] * self.step

    def food_eaten(self, amt=0.5):
        self.step += amt
        self.score += 1
