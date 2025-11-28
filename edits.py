import pygame # imports the pygame module for game development
pygame.init() # initializes all imported pygame modules
from sys import exit # imports the exit function from the sys module
from random import * # Imports all functions, classes, or variables from the random module

screen = pygame.display.set_mode((800, 600)) # set up display window of size 420x420 pixels
pygame.display.set_caption("Flappy Jerry") # sets the window title to "Flappy Jerry"


jerry_alive = pygame.image.load("jerry.png").convert_alpha()
jerry_alive = pygame.transform.scale(jerry_alive, (50, 50))

jerry_position = jerry_alive.get_rect(center = (400, 300)) # get the rectangle of the image and sets the initial position of Jerry

def spacebar():
    jerry_position.y -= 15 # moves Jerry up by 30 pixels
    """Move bird up in response to clicking spacebar."""

running = True
while running:
    jerry_position = jerry_alive.get_rect(center = (400, 300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            spacebar() # calls the spacebar function to move Jerry up

    screen.fill((135, 206, 235))  # light blue background
    screen.blit(jerry_alive, jerry_position)  # draw Jerry
    pygame.display.update()  # update the display

 # makes the bird move down by 5 units in the y-coordinate