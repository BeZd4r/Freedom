import pygame
class Settings:
    
    def __init__(self):

        self.display_width = 800
        self.display_height = 600

        self.bg_image = pygame.transform.scale(pygame.image.load("Sprites/Background.png"), (800,600))
        self.player_image = pygame.transform.scale(pygame.image.load("Sprites/Player.png"), (70,110))
        self.bullet_image = pygame.transform.scale(pygame.image.load("Sprites/Bullet.png"), (10,20))
        self.enemy_image = pygame.transform.scale(pygame.image.load("Sprites/Enemy.png"), (50,80))

        self.player_speed = 0.25
        self.enemy_move_speed = 0.03
        self.enemy_drop_speed = 0.15      
        self.bullet_speed = 0.15

        self.enemy_direction = 1
        self.enemy_strafe_y_range = 40
        self.enemy_speed_mult = 1.1

 