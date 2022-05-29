import pygame
import math

from player import Player
from food import Food
import constants as C
from levels import levels, generate_level
from helpers import Point
from obstacle import Obstacle


def point_inside_rect(point, rect):
    return rect.x <= point.x < rect.x + rect.width and rect.y <= point.y < rect.y + rect.height


def rect_collision(a, b):
    a_points = [
        Point(a.x, a.y), Point(a.x + a.width, a.y), Point(a.x, a.y + a.height), Point(a.x + a.width, a.y + a.height)
    ]
    b_points = [
        Point(b.x, b.y), Point(b.x + b.width, b.y), Point(b.x, b.y + b.height), Point(b.x + b.width, b.y + b.height)
    ]
    for point in a_points:
        if point_inside_rect(point, b):
            return True
    for point in b_points:
        if point_inside_rect(point, a):
            return True
    return False


def collision(player, level):
    for o in levels[level].obstacles:
        if rect_collision(Obstacle(player.x, player.y, player.side, player.side), o):
            return True
    return not (0 <= player.x and player.x + player.side < C.WIDTH
                and 0 <= player.y and player.y + player.side < C.HEIGHT)


def food_ok(food, level):
    not_ok = False
    for o in levels[level].obstacles:
        not_ok = not_ok or point_inside_rect(Point(food.x, food.y), o)
    return not not_ok


def get_food(level):
    food = Food()
    while not food_ok(food, level):
        food = Food()
    return food


def handle_food_overlaps(player, food, level):
    x = food.x + food.side // 2
    y = food.y + food.side // 2
    if player.x <= x < player.x + player.side and player.y <= y < player.y + player.side:
        food = get_food(level)
        player.food_eaten()
    return food


def show_score_message(screen, score, target):
    font = pygame.font.SysFont('Comic Sans MS', 40)
    surface = font.render(str(score) + '/' + str(target), False, (20, 20, 20))
    screen.blit(surface, surface.get_rect())


def redraw(screen, player, food, level):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, player.color, (player.x, player.y, player.side, player.side))
    pygame.draw.rect(screen, food.color, (food.x, food.y, food.side, food.side))
    show_score_message(screen, player.score, levels[level].target)
    for o in levels[level].obstacles:
        pygame.draw.rect(screen, o.color, (o.x, o.y, o.width, o.height))
    inside = 0 <= player.x and player.x + player.side < C.WIDTH and 0 <= player.y and player.y + player.side < C.HEIGHT

def handle_moves(player):
    pressed = pygame.key.get_pressed()
    moved = False
    if pressed[pygame.K_LEFT] and not pressed[pygame.K_RIGHT]:
        player.move(C.LEFT)
        moved = True
    if pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT]:
        player.move(C.RIGHT)
        moved = True
    if pressed[pygame.K_UP] and not pressed[pygame.K_DOWN]:
        player.move(C.UP)
        moved = True
    if pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
        player.move(C.DOWN)
        moved = True
    return moved


def lost_message(screen):
    myfont = pygame.font.SysFont('Comic Sans MS', 70)
    textsurface = myfont.render('Skoda!!', False, (255, 0, 255))
    textrect = textsurface.get_rect(center=(C.WIDTH/2, C.HEIGHT/2))
    screen.blit(textsurface, textrect)


def player_won(player, level):
    return player.score >= levels[level].target


def again(level):
    return Player(), get_food(level)


def main():
    pygame.init()
    pygame.display.set_caption('EatForSpeed')
    pygame.font.init()
    screen = pygame.display.set_mode((C.WIDTH, C.HEIGHT), 0, 32)
    level = 0
    player = Player()
    food = get_food(level)
    redraw(screen, player, food, level)
    running = True
    lost = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player, food = again(level)
                    lost = False
                elif event.key == pygame.K_EQUALS:
                    level += 1
                    generate_level(level)
                    player, food = again(level)
                    lost = False
                elif event.key == pygame.K_MINUS:
                    level = max(0, level - 1)
                    player, food = again(level)
                    lost = False
        if not lost:
            moved = handle_moves(player)
            player.side = player.standing_side
            if moved:
                player.side = int(math.ceil(player.standing_side / math.log2(player.step + 1)))
                diff = player.standing_side - player.side
                player.x += diff // 2
                player.y += diff // 2
            food = handle_food_overlaps(player, food, level)
            redraw(screen, player, food, level)
            collided = collision(player, level)
            if moved:
                player.x -= diff // 2
                player.y -= diff // 2
            if collided:
                lost_message(screen)
                lost = True
            if player_won(player, level):
                level += 1
                generate_level(level)
                player, food = again(level)
                lost = False
        pygame.display.update()


if __name__ == '__main__':
    main()
