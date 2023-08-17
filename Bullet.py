import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):

    def __init__(self, game):

        super().__init__()
        
        self.screen = game.screen
        self.settings = game.settings

        self.speed = game.settings.bullet_speed

        self.bullet_sprite = self.settings.bullet_image
        
        self.rect = self.bullet_sprite.get_rect()
        self.rect.midtop = game.player.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        
        self.y -= self.speed

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.bullet_sprite,self.rect)
