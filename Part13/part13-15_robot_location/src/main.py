import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
robot_x = random.randint(robot.get_width(),640-robot.get_width())
robot_y = random.randint(robot.get_height(),480-robot.get_height())
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if robot_x < event.pos[0] < robot_x + robot.get_width():
                if robot_y < event.pos[1] < robot_y + robot.get_height():
                    robot_x = random.randint(robot.get_width(),640-robot.get_width())
                    robot_y = random.randint(robot.get_height(),480-robot.get_height()) 

        if event.type == pygame.QUIT:
            exit(0)


    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()
    clock.tick(60)