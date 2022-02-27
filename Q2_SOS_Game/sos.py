def printFormat(name_a,name_b,char_a,char_b,score_a,score_b):
    print("-------------------------------------------------------------")
    print(name_a+"'s choice: ",char_a,"\t\tScore of "+name_a+": ",score_a)
    print(name_b+"'s choice: ",char_b,"\t\tScore of "+name_b+": ",score_b)
    print("-------------------------------------------------------------")
    print("\n")
    print("-----------------")
    print("| X | 1 | 2 | 3 |")
    print("| 1 |",list[0][0],"|",list[0][1],"|",list[0][2],"|")
    print("| 2 |",list[1][0],"|",list[1][1],"|",list[1][2],"|")
    print("| 1 |",list[2][0],"|",list[2][1],"|",list[2][2],"|")
    print("-----------------")

print("Welcome to SOS game!\n")
name_a = input("Enter name of 1st player\n")
char_a = input("Enter distinct character for 1st player\n")

list = [["S","X","S"],["S","_","S"],["_","_","_"]]

name_b = input("Enter name of 2nd player\n")
char_b = input("Enter distinct character for 2nd player\n")

printFormat(name_a,name_b,char_a,char_b,100,50)