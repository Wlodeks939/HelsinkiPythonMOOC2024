import pygame


class Game:
    def __init__(self):


        pygame.init()
        self.load_images()
        self.new_game() 

        self.level = 1
        self.level_2 = False 
        self.level_3 = False  
        self.level_4 = False  
        self.level_5 = False  
        self.game_over = False
        self.clock = pygame.time.Clock()
        
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()

        window_height = self.scale * self.height
        window_width = self.scale * self.width
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))
        self.game_font = pygame.font.SysFont("Arial", 24)

        pygame.display.set_caption("Own Game")
        
        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["robot", "coin", "door", "monster"]:
            self.images.append(pygame.image.load(name + ".png"))

    def new_game(self):
        self.map = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8, 9],
                    [9, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]
        self.level = 1
        self.level_2 = False 
        self.level_3 = False  
        self.level_4 = False  
        self.level_5 = False  
        self.game_over = False
        self.points = 0

    def level2(self):
        self.map = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 3, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 8, 2, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]  

    def level3(self):
        self.map = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 3, 1, 1, 1, 1, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 2, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]] 

    def level4(self):
        self.map = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 8, 8, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 3, 8, 8, 1, 1, 8, 8, 8, 8, 9],
                    [9, 0, 8, 8, 8, 8, 3, 8, 8, 8, 1, 1, 8, 8, 8, 2, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]
        
    def level5(self):
        self.map = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]    
        
                    

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            self.monster_move()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move(1, 0)
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.QUIT:
                exit()

    def find_robot(self ):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 0:
                    return (y, x)
        return (0,0)          
                
    def monster_move(self):
        if self.level in [2,3,4]:
            for y in range(self.height):
                for x in range(self.width):
                    if self.map[y][x] == 3 and self.map[y][x - 1] != 9:
                        self.map[y][x - 1] = 3
                        self.map[y][x] = 8
                     

    def move(self, move_y, move_x):

        robot_old_y, robot_old_x = self.find_robot() 
        robot_new_y = robot_old_y + move_y
        robot_new_x = robot_old_x + move_x

        if self.map[robot_new_y][robot_new_x] == 9: # wall collision
            return

        if self.map[robot_new_y][robot_new_x] == 1: # coin collision
            self.map[robot_new_y][robot_new_x] = 8
            self.points += 1

        if self.map[robot_new_y][robot_new_x] == 3: # monster collision 
            
            self.points -= 1

        if self.map[robot_new_y][robot_new_x] == 2: # door collision 
            self.level += 1
            if self.level == 2:
                self.level_2 = True
            elif self.level == 3:
                self.level_3 = True 
            elif self.level == 4:
                self.level_4 = True   
            elif self.level == 5:
                self.level_5 = True
                self.game_over = True          

        self.map[robot_old_y][robot_old_x] = 8 
        self.map[robot_new_y][robot_new_x] = 0 # update robot position                  

    def draw_window(self):

        self.window.fill((0, 0, 0))

        if self.level_2:
            self.level2() 
            self.level_2 = False

        if self.level_3:
            self.level3() 
            self.level_3 = False

        if self.level_4:
            self.level4() 
            self.level_4 = False

        if self.level_5:
            self.level5() 
            self.level_5 = False   
            
            
    

        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] not in [0,1,2,3]: # si no es un png, continua con el siguiente bucle
                    continue
                square = self.map[y][x]
                self.window.blit(self.images[square], (x * self.scale, y * self.scale))

        if not self.game_over:
            game_text = self.game_font.render("Points: " + str(self.points), True, (255, 0, 0))
            self.window.blit(game_text, (25, self.height * self.scale + 10))

            game_text = self.game_font.render("Level: " + str(self.level), True, (255, 0, 0))
            self.window.blit(game_text, (150, self.height * self.scale + 10))

            game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
            self.window.blit(game_text, (300, self.height * self.scale + 10))

            game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
            self.window.blit(game_text, (600, self.height * self.scale + 10))

        if self.game_over:

            game_text = self.game_font.render("GAME OVER", True, (255, 0, 0))
            self.window.blit(game_text, (25, self.height * self.scale + 10))

            game_text = self.game_font.render("Points: " + str(self.points), True, (255, 0, 0))
            self.window.blit(game_text, (150, self.height * self.scale + 10))

            game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
            self.window.blit(game_text, (300, self.height * self.scale + 10))

            game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
            self.window.blit(game_text, (600, self.height * self.scale + 10))

      
        self.clock.tick(5)
        pygame.display.flip()
  

if __name__ == "__main__":
    game = Game()
    game.main_loop()
