import sys
import pygame
from random import randint
from Scripts.Button import Button
from Scripts.Settings import Settings
from Scripts.Player import Player
from Scripts.Enemy import Enemy
from Scripts.Bullet import Bullet
from Scripts.Statistics import Player_kills, Player_Health

class Main:
    
    def __init__(self):

        pygame.init()

        self.settings = Settings()
        pygame.display.set_caption("Freedom")
        pygame.display.set_icon(self.settings.icon_image)

        self.screen = pygame.display.set_mode((self.settings.display_width,
                                               self.settings.display_height))
        
        self.screen_backgroud =self.settings.bg_image
        
        self.bullet_clock = 0
        self.fire = False
        
        
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self._create_enemys()    

        self.kill_stats = Player_kills(self)
        self.health_stats = Player_Health(self)

        self.play_button = Button(self,"Start")
        self.game_active = False

    def _check_ivents(self):

        for event in pygame.event.get():
                
                e = event.type

                if e == pygame.QUIT:
                    sys.exit()

                elif e == pygame.KEYDOWN:
                    self._buttons(event)

                elif e == pygame.KEYUP:
                    self._buttons(event)

                elif e == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True

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
        for row_number in range(randint(1,2)):
            for enemy_number in range(10):
                if randint(0,1):
                    self._create_enemy(enemy_number,row_number)


    def _create_enemy(self,number,row):
        position = (70*number + 50 , 120*row + 75)
        enemy = Enemy(self,position)
        self.enemys.add(enemy)
               
    def _update_bullets(self):
        time = pygame.time.get_ticks()
        if self.fire and  time - self.bullet_clock >= 500:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullet_clock = time
        
        for bullet in self.bullets.sprites():
            bullet.update()

        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet) 

        self._check_enemy_kill()  
    
    def _check_enemy_kill(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.enemys, True , True)
        if collisions:
            self.kill_stats.kills += 1
            if self.kill_stats.kills % 5 == 0:
                if self.settings.speed_mult < 3:
                    self.settings.speed_mult *= 1.1

    def _update_enemys(self):

        for enemy in self.enemys.sprites():
            enemy.update()
            if enemy.rect.bottom >= self.screen.get_rect().bottom:
                self.health_stats.health -= 1
                self.enemys.empty()

        self._check_player_damage()
        self._check_living_enemys()

    def _check_player_damage(self):
        collisions = pygame.sprite.spritecollide(self.player,self.enemys, False)
        if collisions:
            self.health_stats.health -= 1
            self.enemys.empty()

    def _check_living_enemys(self):
        if len(self.enemys.sprites()) == 0:
            self._create_enemys()

    def _update_screen(self):

        self.screen.blit(self.screen_backgroud,(0,0))
        
        
        for bullet in self.bullets.sprites():
            bullet.blitme()

        self.enemys.draw(self.screen)

        self.kill_stats.show_score()
        self.health_stats.show_score()
        
        self.player.blitme()

        if self.health_stats.health == 0:
            self.game_active = False
            self.kill_stats.kills = 0
            self.health_stats.health = 3

        if not self.game_active:
                self.play_button.draw_button()

        pygame.display.flip()
            
    def game_run(self):

        while True:
            self._check_ivents()

            if self.game_active:
                self.player.update()
                self._update_bullets()
                self._update_enemys()

            self._update_screen()

            
if __name__ == "__main__":

    freedom = Main()
    freedom.game_run()