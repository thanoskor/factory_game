import pygame
from machines import Furnace, Belt, Belt_entry, Belt_exit
from tuple_math import Tuple_math

class Build_manager:
    
    def __init__(self):
        self.padding = 10
        self.font = pygame.font.Font(None, 30)
        
        self.modes = ["Furnace", "Belt"]
        self.mode = None

        self.temp_exit = None
        self.temp_entry = None
        
    def draw_ui(self, screen, camera):
        i = 0
        for mode in self.modes:
            i += 1
            text = self.font.render(f"({i}): {mode}", True, (255, 255, 255))
            screen.blit(text, (10, self.padding + 20 * i + (i - 1) * self.padding))
        
        text = self.font.render("Current mode: " + str(self.mode), True, (255, 255, 255))
        screen.blit(text, (0, 0))

        if self.mode != None:
            globals()[self.mode].draw_preview(screen, Tuple_math.add(pygame.mouse.get_pos(), camera), camera)

    def handle_click(self, pos, manager, camera):
        pos = Tuple_math.add(pos, camera)
        if self.mode == None:
            for machine in manager.machines:
                rect = pygame.Rect(machine.pos, (machine.width, machine.height))
                if rect.collidepoint(pos):
                    self.mode = "Furnace"
                    break
        
        if self.mode == "Furnace":
            Furnace(pos, manager)
            self.mode = None
            
        if self.mode == "Belt":
            
            if self.temp_exit == None and self.temp_entry == None:
                for exit in manager.belt_exits:
                        if exit.belt == None and Tuple_math.distance(exit.pos, pos) < exit.radius:
                            self.temp_exit = exit
                            break
                if self.temp_exit == None:
                    for entry in manager.belt_entries:
                        if entry.belt == None and Tuple_math.distance(entry.pos, pos) < entry.radius:
                            self.temp_entry = entry
                            break
            
            else:
                if self.temp_exit == None or self.temp_entry == None:
                    if self.temp_exit == None:
                        for exit in manager.belt_exits:
                                if exit.belt == None and Tuple_math.distance(exit.pos, pos) < exit.radius:
                                    self.temp_exit = exit
                                    break
                    if self.temp_entry == None:
                        for entry in manager.belt_entries:
                            if entry.belt == None and Tuple_math.distance(entry.pos, pos) < entry.radius:
                                self.temp_entry = entry
                                break
                if self.temp_exit != None and self.temp_entry != None:
                    Belt(manager, self.temp_entry, self.temp_exit)
                    self.mode = None
                    self.temp_exit = None
                    self.temp_entry = None
    
    def update(self, input_manager, manager, camera):
        if 3 in input_manager.mouse_press:
            self.mode = None
            self.temp_exit = None
            self.temp_entry = None
            
        elif 1 in input_manager.mouse_press:
            self.handle_click(input_manager.mouse_pos, manager, camera)
        
        elif '1' in input_manager.key_press:
            self.mode = "Furnace"
        elif '2' in input_manager.key_press:
            self.mode = "Belt"