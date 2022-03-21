import random as rnd

def calc(ch1,ch2):
    #all available choices
    list = [1,2,3]
    
    #the door behind to the stone
    stone = rnd.randint(1, 3)
    
    #removing the element whose place has been assigned to the stone
    list.remove(stone)
    
    #selected door
    choice = ch1
    
    if choice != stone:
        list.remove(choice)
        angel = list[0]
        list.remove(angel)
        list.append(stone)
    else:
        angel = rnd.choice(list)
        list.remove(angel)
    
    #choice whether to switch or not
    ch = ch2
    if ch == "y" or ch == "Y":
        choice = list[0]
        
    if choice == stone:
        #Congo! You found the stone
        return 1;
    else:
        #You Lost
        return 0;
    
n = 0
#User, randomly chooses the door and whether to switch or not
for x in range(100):
    n = n + calc(rnd.randint(1, 3),rnd.choice(["Y","N"]))
print("User's Success Rate:",n,"%")

n = 0
#Harry, chooses Door#1 and never switches
for x in range(100):
    n = n + calc(1,"N")
print("Harry's Success Rate:",n,"%")

n = 0
#Ron, chooses Door#1 and always switches
for x in range(100):
    n = n + calc(1,"Y")
print("Ron's Success Rate:",n,"%")