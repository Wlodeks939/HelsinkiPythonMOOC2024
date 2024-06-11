import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x1 = 0
y1 = 480-robot.get_height()
x2 = 20
y2 = 50

to_right1 = False
to_left1 = False
to_up1 = False
to_down1 = False
to_right2 = False
to_left2 = False
to_up2 = False
to_down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_UP:
                to_up1 = True  
            if event.key == pygame.K_DOWN:
                to_down1 = True  

            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_w:
                to_up2 = True  
            if event.key == pygame.K_s:
                to_down2 = True           

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left1 = False
            if event.key == pygame.K_RIGHT:
                to_right1 = False
            if event.key == pygame.K_UP:
                to_up1 = False  
            if event.key == pygame.K_DOWN:
                to_down1 = False      

            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_w:
                to_up2 = False  
            if event.key == pygame.K_s:
                to_down2 = False     

        if event.type == pygame.QUIT:
            exit()

    if to_right1 and (x1 + 2 + robot.get_width()) <= 640:
        x1 += 2
    if to_left1 and x1 - 2 >= 0:
        x1 -= 2
    if to_up1 and y1 - 2 >= 0:
        y1 -= 2
    if to_down1 and (y1 + 2 + robot.get_height()) <= 480:
        y1 += 2   

    if to_right2 and (x2 + 2 + robot.get_width()) <= 640:
        x2 += 2
    if to_left2 and x2 - 2 >= 0:
        x2 -= 2
    if to_up2 and y2 - 2 >= 0:
        y2 -= 2
    if to_down2 and (y2 + 2 + robot.get_height()) <= 480:
        y2 += 2      


    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
