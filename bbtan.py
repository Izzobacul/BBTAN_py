import pygame
import numpy as np

from pygame.math import Vector2

class Element:
    def __init__(self, screen):
        self.screen = screen

class Square(Element):
    def __init__(self, int: num, Vector2: pos):
        self.num = num
        self.pos = pos
        self.size = (WIDTH - sep * 8) / 7

    def show(self, screen):
        screen.draw.rect(screen, (255, 0, 0), (pos.x, pos.y, self.size, self.size))

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def draw(np.ndarray: elements, screen):
    for element in elements:
        element.show(screen)


def main():
    WIDTH, HEIGHT = 360, 640

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    SEP = WIDTH/80

    running = True
    while running:
        running = event_handler()

    pygame.quit()

if __name__ == '__main__':
    main()
