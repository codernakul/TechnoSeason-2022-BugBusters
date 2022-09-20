print("Welcome to the SOS Game..")
while True:
    try:
        board_size = int(input("Plese enter size of the Board: "))
        break
    except:
        print("That's not a valid option!")
#create the board of given size
board = []
for i in range(board_size*board_size):
    board.append("-- ")
    
#prints the board
def printBoard():
    for i in range(board_size*board_size):
        if(i!=0 and i%board_size==0):
            print()
            print()
        print("{:^3}".format(board[i]),end=" ")
    print()
    print()

def printPos():
    for i in range(board_size*board_size):
        if(i!=0 and i%board_size==0):
            print()
            print()
        print("{:^3}".format(str(i)),end=" ")
    print()
    print()
  
#gives the score of the given player   
def scoreCalculator(playerChar):
    score = 0
    
    #horizontal check
    i=0
    while(i<board_size):
        j = board_size*i
        while(j<board_size*(i+1) - 2):
            if(board[j]=="S" and board[j+1]==playerChar and board[j+2]=="S"): 
                score += 10
            j = j+1
        i=i+1
        
    #verticle check
    i=0 
    while(i<board_size-2):
        j = board_size*i
        while(j<board_size*(i+1)):
            if(board[j]=="S" and board[j+board_size]==playerChar and board[j+board_size*2]=="S"):
                score += 10
            j = j+1
        i = i+1
        
    #left right diagonal check
    i=0
    while(i<board_size-2):
        j = board_size*i
        while(j<board_size*(i+1)-2):
            if(board[j]=="S" and board[j + board_size+1]==playerChar and board[j+ board_size*2 + 2] == "S"): 
                score += 10
            j = j+1
        i = i+1
    
    #right left diagonal check
    i=0  
    while(i<board_size-2):
        j=board_size*i + 2
        while(j<board_size*(i+1)):
            if(board[j]=="S" and board[j + board_size-1]==playerChar and board[j + board_size*2 - 2] == "S"):
                score += 10
            j = j+1
        i = i+1 
    return score
    

def boardUpdate(pos,playerChar):
    board[pos] = playerChar
    
#gameplay
printBoard()
print("The positions are as follow: ")
printPos()
p1_name = input("Please enter name of player 1: ")
p1 = input("Enter Player 1's Character: ")
p2_name = input("PLease enter name of player 2: ")
p2 = input("Enter Player 2's Character: ")
player = 1;
for k in range(board_size*board_size):
    print(str(p1_name if player%2==1 else p2_name) + "'s move"+": Please enter position")
    while True:
        try:
            pos = int(input())
            if(pos>=0 and pos<=board_size*board_size - 1):
                break
            else:
                print("Enter a valid option! ")
                continue
        except:
            print("That's not a valid option!")
    if(player%2==1):
        while(True):
            char = input("What do you wanna place at this position ?")
            if(char == "S"):
                boardUpdate(pos,"S")
                break
            elif (char == p1):
                boardUpdate(pos,p1)
                break
            else:
                print("Please enter valid option")
                continue
    else:
        while(True):
            char = input("What do you wanna place at this position ?: ")
            if(char == "S"):
                boardUpdate(pos,"S")
                break
            elif (char == p2):
                boardUpdate(pos,p2)
                break
            else:
                print("Please enter valid option")
                continue
        
    score1 = scoreCalculator(p1)
    score2 = scoreCalculator(p2)
    printBoard()
    print("Player 1 score: " + str(score1))
    print("Player 2 score: " + str(score2))
    player += 1
    
scoreFinal_1 = scoreCalculator(p1)
scoreFinal_2 = scoreCalculator(p2)
if(scoreFinal_1>scoreFinal_2):
    print(p1_name + " is the Winner.")
elif(scoreFinal_2>scoreFinal_1):
    print(p2_name + " is the Winner.")
else:
    print("Game Draw.")

print()
print("END")