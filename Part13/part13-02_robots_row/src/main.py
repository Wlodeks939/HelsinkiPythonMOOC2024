import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))
for i in range(10):
    screen.blit(robot, (50+50*i, 100))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
