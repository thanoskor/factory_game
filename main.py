import pygame
from build_manager import Build_manager
from input_manager import Input_Manager
from entity_manager import Entity_manager
pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

camera = (0, 0)
input_manager = Input_Manager()
build_manager = Build_manager()
entity_manager = Entity_manager()

dt = 0
while True:
    #Inputs
    input_manager.gather_inputs()
    if 'w' in input_manager.key_holding:
        camera = (camera[0], camera[1] - 10)
    if 's' in input_manager.key_holding:
        camera = (camera[0], camera[1] + 10)
    if 'a' in input_manager.key_holding:
        camera = (camera[0] - 10, camera[1])
    if 'd' in input_manager.key_holding:
        camera = (camera[0] + 10, camera[1])
    
    #Logic
    build_manager.update(input_manager, entity_manager, camera)
    
    #Update
    for machine in entity_manager.machines:
        machine.update(dt)
        
    #Render   
    screen.fill((0, 0, 0))
    build_manager.draw_ui(screen, camera)
    for machine in entity_manager.machines:
        machine.draw(screen, camera)
    for belt in entity_manager.belts:
        belt.draw(screen, camera)
        
    #Refresh
    dt = clock.tick(60)
    pygame.display.flip()
    

