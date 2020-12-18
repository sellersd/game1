# First python game

# import pygame module
import pygame
from random import randint as rint

# import pygame locals
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# Constants
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Create a player class
class Player(pygame.sprite.Sprite):
    player_width = 50
    player_height = 50
    player_size = (player_width, player_height)
    player_speed = 5

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('jet.png').convert() # .Surface(self.player_size)
        self.surf.set_colorkey(WHITE, RLEACCEL)
        # self.surf.fill(BLUE)
        self.rect = self.surf.get_rect()
        self.h_loc = SCREEN_WIDTH // 2 - self.player_width // 2
        self.v_loc = SCREEN_HEIGHT // 2 - self.player_height // 2
        self.loc = [self.h_loc, self.v_loc]

    def update(self, pressed_key):
        if pressed_key[K_RIGHT]:
            if self.loc[0] + self.player_width < SCREEN_WIDTH:
                self.loc[0] += self.player_speed
                self.rect.move_ip(self.player_speed, 0)
        elif pressed_key[K_LEFT]:
            if self.loc[0] - self.player_speed >= 0:
                self.loc[0] -= self.player_speed
                self.rect.move_ip(-self.player_speed, 0)
        elif pressed_key[K_UP]:
            if self.loc[1] - self.player_speed >= 0:
                self.loc[1] -= self.player_speed
                self.rect.move_ip(0, -self.player_speed)
        elif pressed_key[K_DOWN]:
            if self.loc[1] + self.player_height < SCREEN_HEIGHT:
                self.loc[1] += self.player_speed
                self.rect.move_ip(0, self.player_speed)


# Create an enemy class extend pygame.sprite.Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load('missle.jpg').convert() # .Surface((20, 10))
        self.surf.set_colorkey(WHITE, RLEACCEL)
        # self.surf.fill(GREEN)
        self.rect = self.surf.get_rect(
            center=(
                rint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                rint(0, SCREEN_HEIGHT),
            )
        )

        self.speed = rint(5, 20)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# initialize game
pygame.init()

# Screen Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# set up screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# custom event for adding enemies
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Create player
player = Player()

# Create groups of sprites
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Run unit user stops
running = True

while running:

    for event in pygame.event.get():
        # Use exit; close window
        # Capture keys pressed
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == ADDENEMY:
            # Create enemy add to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # Update player location based on keys pressed
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update enemy location
    enemies.update()

    # Fill background with light black
    screen.fill((50, 50, 50))

    # Blit sprites to screen
    # screen.blit(player.surf, player.loc)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # check for enemy/player collisions
    if pygame.sprite.spritecollideany(player, enemies):
        # If true, player dead, end game
        player.kill()
        running = False

    # Draw window
    pygame.display.flip()

pygame.quit()
