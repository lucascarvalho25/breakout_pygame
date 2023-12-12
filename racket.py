import pygame
from pygame.locals import Rect

class Racket:
    def __init__(self, screen_width, screen_height, column):
        self.height = 20
        self.width = int(screen_width / column * 2)
        self.original_width = self.width  # Adicione esta linha
        self.x = int((screen_width / 2) - (self.width / 2) + 10)
        self.y = screen_height - (self.height * 2)
        self.speed = 2
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
        self.ball_on_racket = True

    def update_movement(self, screen_width):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

    def draw(self, screen):
        racket_color = (0, 97, 148)
        pygame.draw.rect(screen, racket_color, self.rect)
