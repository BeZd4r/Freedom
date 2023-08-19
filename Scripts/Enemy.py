from random import choice,randint
from pygame.sprite import Sprite

class Enemy(Sprite):

    def __init__(self,game,position):

        super().__init__()

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.screen_width = self.settings.display_width
        self.screen_height = self.settings.display_height
        
        self.image = game.settings.enemy_image
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.speed_x = self.settings.enemy_move_speed
        self.speed_y = self.settings.enemy_drop_speed
        self.speed_mult = self.settings.speed_mult
        self.directiom = choice([-1,1])

        self.strafe_y_flag = False
        self.drop_flag = False

        self.strafe_y_range = self.settings.enemy_strafe_y_range
        self.strafe_range = self.strafe_y_range
        

    def _check_edges(self):
        if self.rect.x <= 0 or self.rect.right >= self.screen_rect.right:
            if self.rect.bottom > self.settings.display_height - 200:
                self.rect.y = 0
                self.y = 0
                self.rect.x = randint(0,self.screen_width)
                self.drop_flag = True
            else:
                self.strafe_y_flag = True
    
    def strafe_y(self):
        if self.strafe_range > 0:    
            self.y += self.speed_y*self.speed_mult
            self.strafe_range -= self.speed_y*self.speed_mult

            self.rect.y = self.y
        else:
            self.strafe_y_flag = False
            self.strafe_range = self.strafe_y_range

            self.directiom *= -1
            self.rect.x += 10* self.directiom

    def move_x(self):
        self.x += self.speed_x * self.directiom * self.speed_mult
        self.rect.x = self.x

    def drop(self):
        self.y += self.speed_y*self.speed_mult/1.5
        self.rect.y = self.y        

    def update(self):
        if self.drop_flag:
            self.drop()
        elif self.strafe_y_flag:
            self.strafe_y()
        else:
            self.move_x()
            self._check_edges()