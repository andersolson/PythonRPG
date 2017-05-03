class Item(object):
    """The base class for all items."""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, 
                                                   self.description, 
                                                   self.value)
class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        super(Gold, self).__init__(name = "Gold",
                         description = "A square coin with {} stamped on the front.".format(str(self.amount)),
                         value = self.amount)
            
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super(Weapon, self).__init__(name, description, value)
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, 
                                                             self.description,
                                                             self.value,
                                                             self.damage)
class Rock(Weapon):
    def __init__(self):
        super(Rock, self).__init__(name = "Rock",
                         description = "A grapefruit sized rock, suitable for bludgeoning",
                         value = 0,
                         damage = 5)
class Dagger(Weapon):
    def __int__(self):
        super(Dagger, self).__init__(name = "Dagger",
                         description = "A small, rusty dagger. A tiny bit more dangerous than a rock.",
                         value = 10,
                         damage = 10)

class superChargedRock(Weapon):
    def __init__(self):
        super(superChargedRock, self).__init__(name = "Super Charged Rock",
                         description = "A large file-cabinet sized rock. Super charged with elemental magic.",
                         value = 10,
                         damage = 20)

    