class Item(object):
    def __init__(self, name, value, quantity = 1):
        self.name = name
        self.raw = name.strip().lower()
        self.quantity = quantity
        
        self.value = value
        self.netValue = quantity * value
        
    def recalc(self):
        self.netValue = self.quantity * self.value

