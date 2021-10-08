import pygame
import sys
import time
import random

#initial game variables
red = pygame.Color(255,0,0)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction

#Parameters for food
food_pos = [0,0]
food_spawn = False

score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))



# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()


def check_for_event():
    global direction
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

        if event.type == pygame.QUIT:
            time.sleep(2)
            pygame.display.quit()
            pygame.quit()
            quit()


def game_over():
    global score
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_texture = my_font.render('Your Score is : ' + str(score), True ,red)
    game_over_rect = game_over_texture.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/2)
    game_window.blit(game_over_texture,game_over_rect,pygame.display.flip())
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()

def update_snake():
    
    global score
    global snake_pos
    global direction
    global food_pos
    global food_spawn


    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10



    #growing mech
    snake_body.insert(0,list(snake_pos))

    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score+=10
        food_spawn = False
    else:
        snake_body.pop()

    #game over
    if snake_pos[0] <0 or snake_pos[0] > frame_size_x-10:

        game_over()
    if snake_pos[1] <0 or snake_pos[1] > frame_size_y-10:

        game_over()

    for block in snake_body[1:]:

        if snake_pos[1] == block[1] and snake_pos[0] == block[0]:

            game_over()


def create_food():

    global food_pos
    global food_spawn

    if not food_spawn:

        food_pos = (random.randrange(1, (frame_size_x//10) )* 10 , random.randrange(1, (frame_size_y//10)) *10)
        food_spawn = True


def show_score(pos, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_texture = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_texture.get_rect()
    game_window.blit(score_texture, score_rect)


def update_screen():
    global snake_body
    global food_spawn
    for pos in snake_body:
        pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    show_score(1, white, 'times new roman', 20)

    pygame.display.update()



while True:
    update_screen()
    check_for_event()
    update_snake()
    create_food()
    game_window.fill(black)
    fps_controller.tick(25)
