from .character import *
from items.container import *


class Player(Character):
    def __init__(self, name, hp, str, int):
        Character.__init__(self, name, hp)
        self.str = str
        self.int = int
        
        self.inventory = {}
        
    def die(self, message="Game Over Loser!"):
        print(message)
        self.hp   = 0
        self.dead = True
        input()