
def cls(lines=100):
    import os
    
    if os.name == "posix":
        os.system("clear")
        
    elif os.name in ("nt", "dos", "ce"):
        os.system("CLS")
    
    else:
        print('\n' * lines)
        
def yesOrNo(prompt="(Y/N)?"):
    while 1:
        answer = raw_input(prompt)
        answer = answer.strip() #remove any symbols
        answer = answer.lower() #change input to be all lower case
        
        yes = ['yes', 'y', 'ye', 'true']
        no  = ['no', 'n', 'nope','false']
        
        if answer in yes: 
            return True
        elif answer in no:
            return False
        else:
            continue #return to beginning of prompt
    
    return False
        