import random as rnd
def choice(a):
    list = [1, 2, 3]

    # the door behind to the stone
    stone = rnd.randint(1, 3)

    # removing the element whose place has been assigned to the stone
    list.remove(stone)

    choice = a

    if choice != stone:
        list.remove(choice)
        angel = list[0]
        list.remove(angel)
        list.append(stone)
    else:
        angel = rnd.choice(list)
        list.remove(angel)

    ch = "N"
    if ch == "y" or ch == "Y":
        choice = list[0]

    if choice == stone:
        print("Congo! You found the stone")
    else:
        print("You Lost")