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
