import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))



robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")
counter = 0

x = 0
y = 480-robot.get_height()

to_right = False
to_left = False
clock = pygame.time.Clock()

number = 100
x_y_lista = [[random.randint(50,580),random.randint(-15000,0)] for number in list(range(number))]
velocity_y_list = [1 for number in list(range(number))] # [1, 1, 1]
eliminado_list = [False for number in list(range(number))] # [False, False, False]


jugar = True
while jugar:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
               

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
           

        if event.type == pygame.QUIT:
            exit()

    if to_right and (x + 2 + robot.get_width()) <= 640:
        x += 2
    if to_left and x - 2 >= 0:
        x -= 2

 
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    for xy in x_y_lista: 
        window.blit(rock, xy)


    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {counter}", True, (255, 0, 0))
    window.blit(text, (400, 20))    
        
    pygame.display.flip()
    
    for i in range(number):
        if not eliminado_list[i]: # solo mueve en eje y a los asteroides que no tocaron al robot
            x_y_lista[i][1] += velocity_y_list[i] # si un asteroide ya toco al robot, deja de moverse en eje y     

    # chequeo colison robot con asteroide
    k = 0
    for xy in x_y_lista:
        if xy[1] + rock.get_height() >= (480 - robot.get_height()) and (x - 20 <= xy[0] <= x + 20 + robot.get_width()):
            counter += 1
            xy[0] = -50 # elimina el asteroide de la pantalla
            eliminado_list[k] = True # esto es para que no le siga aumentando la velocidad en eje y
        k += 1

    # condicion asteroide toca piso, termina juego
    for xy in x_y_lista:
        if xy[1] + rock.get_height() >= 480:
            jugar = False 

    clock.tick(60)
