class Item(object):
    def __init__(self, name, value, quantity = 1):
        self.name = name
        self.raw = name.strip().lower()
        self.quantity = quantity
        
        self.value = value
        self.netValue = quantity * value
        
    def recalc(self):
        self.netValue = self.quantity * self.value
        
        
class Container(object):
    def __init__(self, name):
        self.name = name
        self.inside = {}
        
    def __iter__(self):
        return iter(self.inside.items())
    
    def __len__(self):
        return len(self.inside)
    
    def __contains__(self, item):
        return item.raw in self.inside
    
    def __getitem__(self, item):
        return self.inside[item.raw]
    
    def __setitem__(self, item, value):
        self.inside[item.raw] = value
        return self[item]
    
    def add(self, item, quantity = 1):
        if quantity < 0:
            raise ValueError("Negative quantity. Use remove() instead...")
        
        if item in self:
            self[item].quantity += quantity
            self[item].recalc()
        else:
            self[item] = item
            
    def remove(self, item, quantity = 1):
        if item not in self:
            raise KeyError("Item not in container")
        if quantity < 0: 
            raise ValueError("Negative quantity. Use add() instead...")
        
        if self[item].quantity <= quantity:
            del self.inside[item.raw]
        else:
            self[item].quantity -= quantity
            self[item].recalc()
            
backpack = Container("Backpack")

sword  = Item("Sword", 10)
gold   = Item("Gold Coin", 1, 50)
potion = Item("Potion", 5)

backpack.add(sword)
backpack.add(gold)

def purchase(*items):
    for item in items:
        if item.value > backpack[gold].quantity:
            print("You do not have enough gold!")
            print("Come back when you have {0} more gold.".format(item.value - backpack[gold].quantity))
        else:
            backpack.remove(gold, item.value)
            backpack.add(item)
            print("You purchased '{0}'. You have {1} gold remaining.".format(item.name, backpack[gold].quantity))

#purchase(sword, potion) #You purchased 'Sword'. You have 40 gold remaining. You purchased 'Potion'. You have 35 gold remaining.

#for name, item in backpack:
    #print(name,item) #'gold coin', <__main__.Item object at 0x027B99B0>) 
    #print(item.name,item.quantity) # ('Gold Coin', 50)

#for tuple in backpack:
    #print(tuple[0]) #gold coin, sword
    #print(tuple[1]) #ASCII shit

#print(len(backpack)) #2 (Two items are in backpack)

#print(sword in backpack) #True
#print(gold in backpack) #True
#rint(potion in backpack) #False
