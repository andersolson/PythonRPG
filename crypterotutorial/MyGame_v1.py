import sys
import os
import random

weapons = {"Great Sword":40}
potions = {"Potion":0}

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 200
        self.pot = 0
        self.weap = ["Rusty Sword"]
        self.curWeap = ["Rusty Sword"] 
        
    @property
    def attack(self):
        attack = self.base_attack
        if self.curWeap == "Rusty Sword":
            attack += 5
        
        if self.curWeap == "Great Sword":
            attack += 15
        
        return attack
        
        
class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldGain = 10
GoblinIG = Goblin("Goblin")

class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldGain = 15
ZombieIG = Zombie("Zombie")

class Giant:
    def __init__(self,name):
        self.name = name
        self.maxhealth = 90
        self.health = self.maxhealth
        self.attack = 8
        self.goldGain = 100
GiantIG = Giant("Giant")

def main():
    #os.system('clear')
    os.system("cls") # For windows
    print "Welcome to my game!\n"
    print "1.) Start"
    print "2.) Load"
    print "3.) Exit"
    option = raw_input("-> ")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        main()

def start():
    #os.system('clear')
    os.system("cls") # For windows maybe? or Mac?
    print "Hello, what is your name?"
    option = raw_input("-> ")
    global PlayerIG
    PlayerIG = Player(option)
    start1()
    
def start1():
    #os.system('clear')
    os.system("cls") # For windows maybe? or Mac?
    print "Name: %s" % PlayerIG.name
    print "Attack: %d" % PlayerIG.attack
    print "Health: %i/%i\n" % (PlayerIG.health, PlayerIG.maxhealth)
    print "Gold: %d" % PlayerIG.gold
    print "Current Weapons: %s" % PlayerIG.curWeap
    print "Potions: %d\n" % PlayerIG.pot
    print "1.) Fight"
    print "2.) Store"
    print "3.) Save"
    print "4.) Exit"
    option = raw_input("-> ")
    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        pass
    elif option == "4":
        sys.exit()
    else:
        start1()

def prefight():
    global enemy
    enemynum = random.randint(1, 3)
    if enemynum == 1:
        enemy = GoblinIG
    elif enemynum == 3:
        enemy = GiantIG
    else:
        enemy = ZombieIG
    fight()

        
def fight():
    #os.system('clear')
    os.system('cls')
    print "%s   vs   %s" % (PlayerIG.name, enemy.name)
    print "%s Health: %d/%d   %s Health: %d/%d" % (PlayerIG.name, PlayerIG.health, 
                                                   PlayerIG.maxhealth, enemy.name, 
                                                   enemy.health, enemy.maxhealth)  
    print "Potions: %i\n" % PlayerIG.pot
    print "1.) Attack"
    print "2.) Drink Potion"
    print "3.) Run"
    option = raw_input("-> ")
    if option == "1":
        attack()
    elif option == "2":
        drinkpot()
    elif option == "3":
        run()
    else:
        fight()

def attack():
    #os.system('clear')
    os.system('cls')
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    if PAttack == PlayerIG.attack / 2:
        print "You miss!"
    else:
        enemy.health -= PAttack
        print 'You deal %i damage!' % PAttack
    option = raw_input('-> ')
    if enemy.health <= PAttack:
        win()
    #os.system('clear')
    os.system('cls')
    if EAttack == enemy.attack/2:
        print "The enemy missed!"
    else:
        PlayerIG.health -= EAttack
        print "The enemy deals %i damage!" % EAttack
    option = raw_input('-> ')
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()
    
def drinkpot():
    #os.system('clear')
    os.system('cls')
    if PlayerIG.pot == 0:
        print "You don't have any potions!"
    else:
        PlayerIG.pot -= 1
        PlayerIG.health += 50
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print "You drank a potion"
    option = raw_input('-> ')
    fight()

def run():
    #os.system('clear')
    os.system('cls')
    runnum = random.randint(1, 3) #Have a 1 in 3 chance of running
    if runnum == 1:
        print "You have successfully run away!"
        option = raw_input('-> ')
        start1()
    else:
        print "You failed to escape!"
        option = raw_input('-> ')
        #os.system('clear')
        os.system('cls')
        EAttack = random.randint(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack/2:
            print "The enemy missed!"
        else:
            PlayerIG.health -= EAttack
            print "The enemy deals %i damage!" % EAttack
        option = raw_input('-> ')
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()
         
def win():
    #os.system('clear')
    os.system('cls')
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.goldGain
    print "You have defeated the %s" % enemy.name
    print "You found %i gold!" % enemy.goldGain
    option = raw_input('-> ')
    start1()

def dead():
    #os.system('clear')
    os.system('cls')
    print "You have died"
    option = raw_input('-> ')
    
def store():
    #os.system('clear')
    os.system('cls')
    print "Welcome to the shop!"
    print "\n What would you like to buy?"
    print "> Great Sword: 40 gold"
    print "> Potion: 20 gold"
    print "\n> Leave Store"
    print " "
    option = raw_input("-> ")
    
    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            #os.system('clear')
            os.system('cls')
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print "You have purchased %s" % option
            option = raw_input('-> ')
            store()
            
        else:
            #os.system('clear')
            os.system('cls')
            print "You do not have enough gold for that."
            option = raw_input('-> ')
            store()
    
    elif option in potions:
        #os.system('clear')
        os.system('cls')
        PlayerIG.gold -= potions[option]
        PlayerIG.pot += 1
        print "You have purchased %s" % option
        option = raw_input('-> ')
        store()
    
    elif option == "Leave Store":
        start1()
        
    else:
        print "That item does not exist"
        option = raw_input('-> ')
        store()

    
main()
    