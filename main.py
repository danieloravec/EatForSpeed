import pygame

from player import Player
from food import Food
import constants as C


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
    inside = 0 <= player.x and player.x + player.side < C.WIDTH and 0 <= player.y and player.y + player.side < C.HEIGHT
    if not inside:
        return False
    return True


def handle_moves(player):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
        player.move(C.UP_RIGHT)
    elif pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
        player.move(C.UP_LEFT)
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT]:
        player.move(C.DOWN_RIGHT)
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
        player.move(C.DOWN_LEFT)
    elif pressed[pygame.K_LEFT]:
        player.move(C.LEFT)
    elif pressed[pygame.K_RIGHT]:
        player.move(C.RIGHT)
    elif pressed[pygame.K_UP]:
        player.move(C.UP)
    elif pressed[pygame.K_DOWN]:
        player.move(C.DOWN)


def lost_message(screen, score):
    myfont = pygame.font.SysFont('Comic Sans MS', 70)
    textsurface = myfont.render('Mas iba ' + str(score) + ' bodou :(', False, (255, 0, 255))
    textrect = textsurface.get_rect(center=(C.WIDTH/2, C.HEIGHT/2))
    screen.blit(textsurface, textrect)


def again():
    return Player(), Food()


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((C.WIDTH, C.HEIGHT), 0, 32)
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
