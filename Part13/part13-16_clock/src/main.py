import pygame
import math

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

class Clock:
    def __init__(self,hours,minutes,seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
      
    def tick(self):
        self.seconds += 1
        if  self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.seconds = 0
            self.minutes = 0 
            self.hours += 1
        if self.hours == 24:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0

    def string(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"     

time = Clock(15,0,0)        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    

    x_seg = 320 + math.cos(0.10466 * time.seconds - 1.57)*180
    y_seg = 240 + math.sin(0.10466 * time.seconds - 1.57)*180

    x_min = 320 + math.cos(0.10466 * time.minutes - 1.57)*160
    y_min = 240 + math.sin(0.10466 * time.minutes - 1.57)*160

    x_hr = 320 + math.cos(0.10466 * time.hours - 1.57 )*140
    y_hr = 240 + math.sin(0.10466 * time.hours - 1.57 )*140

    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 10) # si omitis width lo rellena
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 200, width=4) #color, xy del centro, radio, grosor

    pygame.draw.line(display, (0, 0, 255), (320, 240), (x_seg, y_seg), 2) #seg
    pygame.draw.line(display, (0, 0, 255), (320, 240), (x_min, y_min), 4) #min
    pygame.draw.line(display, (0, 0, 255), (320, 240), (x_hr, y_hr), 6) #hour
    
    pygame.display.flip()
    time.tick()  # agrega 1 seg al objeto time 
    clock.tick(1) #actualiza cada 1 seg
    pygame.display.set_caption(time.string()) # actualiza titulo con la nueva hora
