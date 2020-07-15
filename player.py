import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.screen = screen

    def damage(self, amount):
        if self.health - amount >= 0:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60,60,60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x + 50, self.rect.y + 20, self.health, 5]) 

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        if self.rect.x + self.rect.width < self.screen.get_width() and not self.game.check_collision(self, self.game.all_monsters): 
            self.rect.x += self.velocity

    def move_left(self):
        if self.rect.x > 0 : self.rect.x -= self.velocity