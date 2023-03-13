#run "pip install pygame, pygame_gui" if there is an error
#run game with "python main.py"
import pygame
import random
import pygame_gui

import tkinter as tk
from tkinter import messagebox

pygame.init()
pygame.font.init()

pygame.display.set_caption("Tybik?????????")

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 36)
white = (255, 255, 255)
black = (0, 0, 0)


def game():
    global score, game_over

    # positions of tybiks
    player_x = screen_width / 2
    player_y = screen_height - 50
    player_width = 50
    player_height = 50

    enemy_x = random.randint(0, screen_width - player_width)
    enemy_y = 0
    enemy_width = 50
    enemy_height = 50
    enemy_speed = 0.2

    bullet_x = 0
    bullet_y = 0
    bullet_width = 5
    bullet_height = 20
    bullet_speed = 10
    game_over = False
    score = 0

    while not game_over:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet_x = player_x + player_width / 2 - bullet_width / 2
                    bullet_y = player_y - bullet_height

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= 0.5
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += 0.5

        # enemy move
        enemy_y += enemy_speed

        if enemy_y > screen_height:
            enemy_x = random.randint(0, screen_width - player_width)
            enemy_y = 0

        # player hit
        if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and player_y < enemy_y + enemy_height and player_y + player_height > enemy_y:
            game_over = True

        # bullet hit
        if bullet_x < enemy_x + enemy_width and bullet_x + bullet_width > enemy_x and bullet_y < enemy_y + enemy_height and bullet_y + bullet_height > enemy_y:
            enemy_x = random.randint(0, screen_width - player_width)
            enemy_y = 0
            score += 1

        # drawer
        screen.fill(white)
        pygame.draw.rect(screen, black, [player_x, player_y, player_width, player_height])
        pygame.draw.rect(screen, black, [enemy_x, enemy_y, enemy_width, enemy_height])
        pygame.draw.rect(screen, black, [bullet_x, bullet_y, bullet_width, bullet_height])
        score_text = font.render("Score: " + str(score), True, black)
        screen.blit(score_text, [10, 10])

        # bullet up
        if bullet_y > 0:
            bullet_y -= bullet_speed
        else:
            bullet_x = 0
            bullet_y = 0

        # Update
        pygame.display.update()

    return score

def show_message_box(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)


play_again = True

while play_again:
    score = game()
