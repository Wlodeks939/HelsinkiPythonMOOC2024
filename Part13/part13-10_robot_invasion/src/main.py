import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

number = 150

x_y_lista = [[random.randint(50,580),random.randint(-8000,0)] for number in list(range(number))]
velocity_x_list = [0 for number in list(range(number))] # [0, 0, 0]
velocity_y_list = [1 for number in list(range(number))] # [1, 1, 1]
toco_piso_list = [False for number in list(range(number))] # [False, False, False]
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for xy in x_y_lista: 
        window.blit(robot, xy)
        
    pygame.display.flip()
    
    for i in range(number):
        x_y_lista[i][1] += velocity_y_list[i]     
        x_y_lista[i][0] += velocity_x_list[i]     
     

    for i in range(number):
        if x_y_lista[i][1]+robot.get_height() >= 480 and not toco_piso_list[i]:
            
            velocity_x_list[i] = random.choice([1,-1])
            velocity_y_list[i] = 0
            toco_piso_list[i] = True

    clock.tick(60)
