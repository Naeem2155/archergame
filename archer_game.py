# -*- coding: utf-8 -*-
"""archer_game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pWy_nSiPay9xDmBFEdVMl7IyY8UNHSiO
"""

import pygame
import random
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Archer Game")
class Archer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("archer.png")  # Replace with your archer image
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)

class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("arrow.png")  # Replace with your arrow image
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 70)
        self.speed = 5  # Adjust arrow speed as needed

    def update(self):
        self.rect.y -= self.speed
archer = Archer()
arrow_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(archer)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                arrow = Arrow()
                arrow_group.add(arrow)
                all_sprites.add(arrow)

    # Update
    arrow_group.update()

    # Draw
    screen.fill((255, 255, 255))  # Fill the screen with white color
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()