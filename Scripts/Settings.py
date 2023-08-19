import pygame
class Settings:
    
    def __init__(self):

        self.display_width = 800
        self.display_height = 600

        self.icon_image = pygame.image.load("Sprites/icon.png")
        self.bg_image = pygame.transform.scale(pygame.image.load("Sprites/Background.png"), (800,600))
        self.player_image = pygame.transform.scale(pygame.image.load("Sprites/Player.png"), (70,110))
        self.bullet_image = pygame.transform.scale(pygame.image.load("Sprites/Bullet.png"), (10,20))
        self.enemy_image = pygame.transform.scale(pygame.image.load("Sprites/Enemy.png"), (50,80))
        self.kill_statistic_image = pygame.transform.scale(pygame.image.load("Sprites/Enemy_kill.png"),(45,60))
        self.player_health_image = pygame.transform.scale(pygame.image.load("Sprites/Player_health.png"),(45,60))

        self.player_speed = 0.25
        self.bullet_speed = 0.15

        self.enemy_move_speed = 0.15
        self.enemy_drop_speed = 0.2    
        self.enemy_strafe_y_range = 40
        self.speed_mult = float(1.1)

        self.player_lives = 3

        

 