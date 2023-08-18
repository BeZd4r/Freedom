import pygame

class Player:

    def __init__(self,game):

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect  = self.screen.get_rect()

        self.sprite = self.settings.player_image
        self.rect = self.sprite.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.speed = self.settings.player_speed
        self.speed_mult = self.settings.speed_mult
        self.mright = False
        self.mleft = False

    def blitme(self):
        self.screen.blit(self.sprite, self.rect)

    def update(self):

        if self.mleft and self.rect.left > 0:
            self.x -= self.speed*self.speed_mult

        elif self.mright and self.rect.right < self.screen_rect.right:
            self.x += self.speed*self.speed_mult

        self.rect.x = self.x

