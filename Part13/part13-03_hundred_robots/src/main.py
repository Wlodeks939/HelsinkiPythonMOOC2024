import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))
shift = 0
for j in range(10):  
    for i in range(10):  
        screen.blit(robot, (30+40*i + shift, 30+30*j))
    shift += 11
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

