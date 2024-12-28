import pygame

class Entity_manager:
    def __init__(self):
        self.machines = []
        
        self.belts = []
        self.belt_entries = []
        self.belt_exits = []
        
    def add_machine(self, machine):
        self.machines.append(machine)
    
    def add_belt_entry(self, belt_entry):
        self.belt_entries.append(belt_entry)
        
    def add_belt_exit(self, belt_exit):
        self.belt_exits.append(belt_exit)
    
    def add_belt(self, belt):
        self.belts.append(belt)