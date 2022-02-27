import random as rnd

#all available choices
list = [1,2,3]

#the door behind to the stone
stone = rnd.randint(1, 3)

#removing the element whose place has been assigned to the stone
list.remove(stone)

#print(stone)
#print(list)

print("The Angel has put the Philosopher's Stone behind one of the doors,\nNow you must choose one out of them wisely!")

choice = int(input("Enter choice out of gate no. #1 #2 #3\n"))

if choice != stone:
    list.remove(choice)
    angel = list[0]
    list.remove(angel)
    list.append(stone)
else:
    angel = rnd.choice(list)
    list.remove(angel)

print("The angel opened the Door #",angel,"\nBut Unfortunately The Philosophers Stone was not there ;-;\n")

ch = input("Would you like to switch your choice (Y/N)")
if ch == "y" or ch == "Y":
    choice = list[0]
    
if choice == stone:
    print("Congo! You found the stone")
else:
    print("You Lost")

#print(angel)
#print(list)