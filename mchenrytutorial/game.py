#Main game file
from characters.player import * # Import player from the characters folder
from commands import * #Import everything in the commands script
from utilities.util import * #Import everything from util script

def help(player, args):
    for command in commands:
        print(command)
        
#def help(player, args):
    #print "test"
    #print player.name
    #print player.hp

commands = {
    'help' : help,
    'exit' : exit,
    'quit' : exit,
}

player = Player("Default", 1, 1, 1)

def nameInput(prompt):
    name = raw_input(prompt) #Input needs to be raw
    return name.strip() #Remove any symbols in the name 

def getName():
    tempName = ""
    while 1:
        tempName = nameInput("What is your name? ")
        
        if len(tempName) < 1: #if the input is less than 1 character ask for name again
            continue
        
        yes = yesOrNo(tempName + ", is that your name? ")
        
        if yes:
            return tempName
        else:
            continue

def isValidCMD(cmd):
    if cmd in commands:
        return True
    return False

def runCMD(cmd, args, player):
    commands[cmd](player, args)

def main(player):
    
    player.name = getName() #Call getName function to get user input
    
    while (not player.dead):
        line = raw_input(">> ")
        input = line.split()
        input.append("EOI")
        
        if isValidCMD(input[0]):
            runCMD(input[0], input[1], player)

main(player)