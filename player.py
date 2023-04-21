class Player:
    def __init__(self):
        self.x = 2
        self.y = 2
        self.standing_side = 50
        self.side = self.standing_side
        self.step = 1
        self.dx = (0, 1, 1, 1, 0, -1, -1, -1)
        self.dy = (-1, -1, 0, 1, 1, 1, 0, -1)
        self.color = (0, 255, 0)
        self.score = 0

    def move(self, direction):
        self.x += self.dx[direction] * self.step
        self.y += self.dy[direction] * self.step

    def food_eaten(self, amt=0.33):
        self.step += amt
        self.score += 1
