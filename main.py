import pygame
from random import randint


UP = 0
UP_RIGHT = 1
RIGHT = 2
DOWN_RIGHT = 3
DOWN = 4
DOWN_LEFT = 5
LEFT = 6
UP_LEFT = 7

WIDTH = 1000
HEIGHT = 600


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

    def increase_speed(self, amt=0.5):
        self.step += amt
        self.score += 1


class Food:
    def __init__(self):
        # TODO avoid generating food inside a player
        self.x = randint(100, WIDTH - 100)
        self.y = randint(100, HEIGHT - 100)
        self.side = 10
        self.color = (255, 0, 0)


def handle_overlaps(player, food):
    x = food.x + food.side // 2
    y = food.y + food.side // 2
    if player.x <= x < player.x + player.side and player.y <= y < player.y + player.side:
        food = Food()
        player.increase_speed()
    return food


def redraw(screen, player, food):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, player.color, (player.x, player.y, player.side, player.side))
    pygame.draw.rect(screen, food.color, (food.x, food.y, food.side, food.side))
    inside = 0 <= player.x and player.x + player.side < WIDTH and 0 <= player.y and player.y + player.side < HEIGHT
    if not inside:
        return False
    return True


def handle_moves(player):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
        player.move(UP_RIGHT)
    elif pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
        player.move(UP_LEFT)
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT]:
        player.move(DOWN_RIGHT)
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
        player.move(DOWN_LEFT)
    elif pressed[pygame.K_LEFT]:
        player.move(LEFT)
    elif pressed[pygame.K_RIGHT]:
        player.move(RIGHT)
    elif pressed[pygame.K_UP]:
        player.move(UP)
    elif pressed[pygame.K_DOWN]:
        player.move(DOWN)


def lost_message(screen, score):
    myfont = pygame.font.SysFont('Comic Sans MS', 70)
    textsurface = myfont.render('Mas iba ' + str(score) + ' bodou :(', False, (255, 0, 255))
    textrect = textsurface.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(textsurface, textrect)


def again():
    return Player(), Food()


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    player = Player()
    food = Food()
    redraw(screen, player, food)
    running = True
    lost = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player, food = again()
                    lost = False
        if not lost:
            handle_moves(player)
            food = handle_overlaps(player, food)
            if not redraw(screen, player, food):
                lost_message(screen, player.score)
                lost = True
        pygame.display.update()


if __name__ == '__main__':
    main()
