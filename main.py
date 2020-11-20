# First python game

# import pygame module
import pygame

# import pygame locals
from pygame.locals import (
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
    player_speed = 25

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Player, self).__init__()
        self.surf = pygame.Surface(self.player_size)
        self.surf.fill(BLUE)
        self.rect = self.surf.get_rect()
        self.h_loc = SCREEN_WIDTH // 2 - self.player_width//2
        self.v_loc = SCREEN_HEIGHT // 2 - self.player_height//2
        print(self.v_loc)
        self.loc = [self.h_loc, self.v_loc]

    def update(self, pressed_key):
        if pressed_key[K_RIGHT]:
            if self.h_loc + self.player_width < SCREEN_WIDTH:
                self.loc[0] += self.player_speed
                self.rect.move_ip(self.player_speed, 0)
        elif pressed_key[K_LEFT]:
            if self.h_loc - self.player_speed >= 0:
                self.loc[0] -= self.player_speed
                self.rect.move_ip(-self.player_speed, 0)
        elif pressed_key[K_UP]:
            if self.v_loc - self.player_speed >= 0:
                self.loc[1] -= self.player_speed
                self.rect.move_ip(0, -self.player_speed)
        elif pressed_key[K_DOWN]:
            if self.loc[1] + self.player_height < SCREEN_HEIGHT:
                self.loc[1] += self.player_speed
                self.rect.move_ip(0, self.player_speed)



# initialize game
pygame.init()

# Screen Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# h_loc = SCREEN_WIDTH//2
# v_loc = SCREEN_HEIGHT//2
# circle_loc = [h_loc, v_loc]

# set up screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# player = pygame.Surface((player_width, player_height))
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

# Run unit user stops
running = True

while running:

    for event in pygame.event.get():
        # Use exit; close window
        # Capture keys pressed
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
           #  elif event.key == K_RIGHT:
           #      if player.loc[0] + player.player_width < SCREEN_WIDTH:
           #          # h_loc = h_loc + player.player_speed
           #          player.update(K_RIGHT)
           #  elif event.key == K_LEFT:
           #      if player.loc[0] - player.player_speed >= 0:
           #          # h_loc = h_loc - player.player_speed
           #          player.update(K_LEFT)
           #  elif event.key == K_UP:
           #      if player.loc[1] - player.player_speed >= 0:
           #          # v_loc = v_loc - player.player_speed
           #          player.update(K_UP)
           #  elif event.key == K_DOWN:
           #      if player.loc[1] + player.player_speed < SCREEN_HEIGHT:
           #          # v_loc = v_loc + player.player_speed
           #          player.update(K_DOWN)

    # Update player location based on keys pressed
    player.update(pressed_keys)

    # Fill background with light black
    screen.fill((50, 50, 50))

    # Blit player to screen
    screen.blit(player.surf, player.loc)

    # Draw window
    pygame.display.flip()

pygame.quit()
