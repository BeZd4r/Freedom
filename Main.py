import sys
import pygame
from Settings import Settings
from Player import Player
from Enemy import Enemy
from Bullet import Bullet

class Main:
    
    def __init__(self):

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.display_width,
                                               self.settings.display_height),display=0)

        self.screen_backgroud =self.settings.bg_image
        
        self.bullet_clock = 0
        self.enemy_direction = self.settings.enemy_direction
        self.fire = False
        
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self._create_enemys()

        
        

    def _check_ivents(self):

        for event in pygame.event.get():
                
                e = event.type

                if e == pygame.QUIT:
                    sys.exit()

                elif e == pygame.KEYDOWN:
                    self._buttons(event)

                elif e == pygame.KEYUP:
                    self._buttons(event)

    def _buttons(self,event):

        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.player.mleft =  not self.player.mleft

        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.player.mright = not self.player.mright

        if event.key == pygame.K_SPACE:
            self.fire = not self.fire

        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _create_enemys(self):
        for row_number in range(3):
            for enemy_number in range(4):
                self._create_enemy(enemy_number,row_number)
            self.enemy_direction *= -1

    def _create_enemy(self,number,row):
        position = (50*number +50, 80*row + 80)
        enemy = Enemy(self,position)
        self.enemys.add(enemy)
               
    def _update_bullets(self):
        time = pygame.time.get_ticks()
        if self.fire and  time - self.bullet_clock >= 750:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullet_clock = time
        
        for bullet in self.bullets.sprites():
            bullet.update()

        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)   


    def _update_enemys(self):
        for enemy in self.enemys.sprites():
            enemy.update()
            
        
    def _update_screen(self):

        self.screen.blit(self.screen_backgroud,(0,0))
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.blitme()

        self.enemys.draw(self.screen)

        pygame.display.flip()
            
    def game_run(self):

        while True:
            self._check_ivents()
            self.player.update()
            self._update_bullets()
            self._update_enemys()

            self._update_screen()

if __name__ == "__main__":

    freedom = Main()
    freedom.game_run()