import pygame
pygame.init()

from tuple_math import Tuple_math

class Slot:
    def __init__(self):
        self.item = None
        self.amount = 0
    
    def add_item(self, item, amount):
        if self.item == None:
            self.item = item
            self.amount = amount
            return True
        elif self.item == item:
            self.amount += amount
            return True
        else:
            return False
    
    def remove_item(self, amount):
        if self.amount < amount:
            return False
        self.amount -= amount
        if self.amount == 0:
            self.item = None
        return True
        
class Machine:
    def __init__(self, pos, manager):
        self.manager = manager
        self.manager.add_machine(self)
        
        self.pos = pos
        self.progress = 0
        self.recipe = None
        self.exit_slot = Slot()
        self.proces_slot = Slot()
    
    def draw(self, screen, camera):
        pass
    
    def draw_preview(screen, pos, camera):
        pass
    
    def update(self, dt):
        pass        

class Belt_entry:
    radius = 10
    color = (0, 0, 255)
    def __init__(self, machine, manager, relative_pos):
        self.manager = manager
        self.manager.add_belt_entry(self)
        self.machine = machine
        
        self.belt = None
        self.pos = Tuple_math.add(machine.pos, relative_pos)

    def draw(self, screen, camera):
        pygame.draw.circle(screen, Belt_entry.color, Tuple_math.sub(self.pos, camera), Belt_entry.radius)

    def update(self, dt):
        pass
    
class Belt_exit:
    radius = 10
    color = (0, 255, 0)
    def __init__(self, machine, manager, relative_pos):
        self.manager = manager
        self.manager.add_belt_exit(self)
        self.machine = machine
        
        self.belt = None
        self.pos = Tuple_math.add(machine.pos, relative_pos)
        
    def draw(self, screen, camera):
        pygame.draw.circle(screen, Belt_exit.color, Tuple_math.sub(self.pos, camera), Belt_exit.radius)

    def update(self, dt):
        pass

class Belt:
    width = 10
    color = (255, 255, 255)
    def __init__(self, manager, entry, exit):
        self.manager = manager
        self.manager.add_belt(self)
        
        self.entry = entry
        self.exit = exit
        
        self.entry.belt = self
        self.exit.belt = self
    
    def draw(self, screen, camera):
        pygame.draw.line(screen, Belt.color, Tuple_math.sub(self.entry.pos, camera), Tuple_math.sub(self.exit.pos, camera), Belt.width)
    
    def draw_preview(screen, pos, camera):
        pass
    
    def update(self, dt):
        pass

class Furnace(Machine):
    width = 50
    height = 100
    
    rect_color = (255, 0, 0)
    preview_color = (200, 0, 0)
    
    font = pygame.font.Font(None, 20)

    def __init__(self, pos, manager):
        super().__init__(pos, manager)
        self.entry = Belt_entry(self, manager, (-25, 0))
        self.exit = Belt_exit(self, manager, (25, 0))
        
    def draw(self, screen, camera):
        pos = Tuple_math.sub(Tuple_math.sub(self.pos, camera), (self.width // 2, self.height // 2))
        rect = (pos, (self.width, self.height))
        pygame.draw.rect(screen, self.rect_color, rect)
        self.exit.draw(screen, camera)
        self.entry.draw(screen, camera)
        
        text = Furnace.font.render(f"{self.recipe}", True, (255, 255, 255))
        screen.blit(text, (pos[0], pos[1] - 10))
        
    def draw_preview(screen, pos, camera):
        p = Tuple_math.sub(Tuple_math.sub(pos, camera), (Furnace.width // 2, Furnace.height // 2))
        rect = (p, (Furnace.width, Furnace.height))
        pygame.draw.rect(screen, Furnace.preview_color, rect)
    
    def update(self, dt):
        pass