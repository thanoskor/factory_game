import pygame
from sys import exit

class Input_Manager:
    def __init__(self):
        
        self.key_press = set()
        self.key_holding = set()

        self.mouse_pos = (0, 0)
        self.mouse_press = set()
        self.mouse_holding = set()

    def gather_inputs(self):
        self.key_press.clear()
        self.mouse_press.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.key_press.add(pygame.key.name(event.key))
                self.key_holding.add(pygame.key.name(event.key))
            if event.type == pygame.KEYUP:
                self.key_holding.remove(pygame.key.name(event.key))
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_press.add(event.button)
                self.mouse_holding.add(event.button)
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_holding.remove(event.button)

        self.mouse_pos = pygame.mouse.get_pos()