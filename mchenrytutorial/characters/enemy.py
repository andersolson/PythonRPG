
from character import *

class Enemy(Character):
    def __init__(self, name, hp, str):
        Character.__init__(self, name, hp)
        self.str = str