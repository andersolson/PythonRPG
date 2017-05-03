class Enemy(object):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def is_alive(self):
        return self.hp > 0
    
class GiantSpider(Enemy):
    def __init__(self, name, hp, damage):
        super(Enemy, self).__init__(name="Giant Spider",hp=10,damage=2)

class Ogre(Enemy):
    def __init__(self):
        super(Ogre,self).__init__(name = "Ogre",
                         hp = 30,
                         damage = 15)

class lettuce(Enemy):
    def __init__(self):
        super(lettuce, self).__init__(name = "Lettuce",
                         hp = 100,
                         damage = 0)