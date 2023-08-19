import pygame.font

class Player_kills:

    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.icon_image = game.settings.kill_statistic_image
        self.icon_rect = self.icon_image.get_rect()
        self.icon_rect.right = self.screen_rect.right - 75
        self.icon_rect.top = self.screen_rect.top

        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,30) 

        self.kills = 0

        self.prep_score()
        self.show_score()

    def prep_score(self):
        kills = str(self.kills)
        self.kills_image = self.font.render(kills,True,self.text_color)

        self.text_rect = self.kills_image.get_rect()
        self.text_rect.right = self.icon_rect.right - 1
        self.text_rect.bottom = self.icon_rect.bottom + 2
            
    def show_score(self):
        self.prep_score()
        self.screen.blit(self.icon_image,self.icon_rect)
        self.screen.blit(self.kills_image, self.text_rect)

class Player_Health:

    def __init__(self, game):

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.health_image = self.settings.player_health_image
        self.image_rect = self.health_image.get_rect()
        self.image_rect.right = self.screen_rect.right - 10
        self.image_rect.top = self.screen_rect.top

        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,30) 

        self.health = self.settings.player_lives

        self.prep_score()
        self.show_score()

    def prep_score(self):
        health = str(self.health)
        self.health_text = self.font.render(health, True,self.text_color)

        self.text_rect = self.health_text.get_rect()
        self.text_rect.right = self.image_rect.right - 1
        self.text_rect.bottom = self.image_rect.bottom + 2
    
    def show_score(self):
        self.prep_score()
        self.screen.blit(self.health_image,self.image_rect)
        self.screen.blit(self.health_text, self.text_rect)
