# Python Version : 3.9
# Pygmae Version : 2.0.0
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#


import pygame
import sys
import random
import time

# START PYGAME MODULES
pygame.init()

# ALL VARIABLE
display_width = 576
display_height = 1024
floor_x = 0
gravity = 0.25
bird_movement = 0
pipe_list = []
game_status = True
bird_list_index = 0
game_font = pygame.font.Font('assets/font/Flappy.TTF', 40)
score = 0
high_score = 0
active_score = True

# ---------- #
create_pipe = pygame.USEREVENT
create_flap = pygame.USEREVENT + 1
pygame.time.set_timer(create_flap, 100)
pygame.time.set_timer(create_pipe, 1200)
# ---------- #
win_sound = pygame.mixer.Sound('assets/sound/smb_stomp.wav')
game_over_sound = pygame.mixer.Sound('assets/sound/smb_mariodie.wav')
# ---------- #
background_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/bg2.png'))
floor_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/floor.png'))
bird_image_down = pygame.transform.scale2x(
    pygame.image.load('assets/img/red_bird_down_flap.png'))
bird_image_mid = pygame.transform.scale2x(
    pygame.image.load('assets/img/red_bird_mid_flap.png'))
bird_image_up = pygame.transform.scale2x(
    pygame.image.load('assets/img/red_bird_up_flap.png'))
bird_list = [bird_image_down, bird_image_mid, bird_image_up]
bird_image = bird_list[bird_list_index]
pipe_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/pipe_red.png'))
game_over_image = pygame.transform.scale2x(
    pygame.image.load('assets/img/message.png'))
game_over_image_rect = game_over_image.get_rect(center=(288, 512))
