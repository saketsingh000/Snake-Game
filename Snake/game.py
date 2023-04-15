# import lib
import pygame
import time
import random

speed = 17

window_x = 720
window_y = 500

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

#
pygame.init()

pygame.display.set_caption("Snake Code With Durgesh")
window = pygame.display.set_mode((window_x, window_y))

snake_position = [100, 60]
snake_body = [[100, 60], [90, 60], [80, 60], [70, 60]]


# generate random food position
def generate_random_food_position():
    return [
        random.randrange(1, (window_x // 10) * 10),
        random.randrange(1, (window_y // 10) * 10)
    ]


food_position = generate_random_food_position()

direction = 'RIGHT'

score = 0


def show_score(choice, color, font, size):
    s_font = pygame.font.SysFont(font, size)
    s_surface = s_font.render("SCORE : " + str(score), True, color)
    s_rect = s_surface.get_rect()
    window.blit(s_surface, s_rect)


def game_over():
    font = pygame.font.SysFont("Roboto", 50)
    go_surface = font.render("YOUR SCORE IS " + str(score), True, blue)
    go_rect = go_surface.get_rect()
    go_rect.midtop = (window_x / 2, window_y / 4)
    window.blit(go_surface, go_rect)

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()

    quit()


fps = pygame.time.Clock()

while True:
    # events handle karne honge
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 'DOWN':
                    direction = 'UP'
            if event.key == pygame.K_DOWN:
                if direction != 'UP':
                    direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                if direction != 'RIGHT':
                    direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                if direction != 'LEFT':
                    direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == "RIGHT":
        snake_position[0] = snake_position[0] + 10

    # body grow
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1] or pygame.Rect(food_position[0],food_position[1],10,10).collidepoint(snake_position[0],snake_position[1]) :
        score += 10
        food_position = generate_random_food_position()
    else:
        snake_body.pop()

    window.fill(black)

    for sb in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(sb[0], sb[1], 20, 20))

    pygame.draw.rect(window, white, pygame.Rect(food_position[0], food_position[1], 20, 20))

    # game over
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    show_score(1, white, "Robot", 40)

    pygame.display.update()

    fps.tick(speed)