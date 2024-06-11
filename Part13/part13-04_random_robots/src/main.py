import pygame
import random
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()

for i in range(1000):  

    x = random.randint(0,640-width)
    y = random.randint(0,480-height)
    screen.blit(robot, (x, y))
    
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

