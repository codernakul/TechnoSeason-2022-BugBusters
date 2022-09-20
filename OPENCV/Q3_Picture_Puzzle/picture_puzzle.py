import cv2
import numpy as np
import random as rnd
from os.path import exists

order = []
#no of pieces to be divided in
imagePath = input("Enter image path: ")
while not exists(imagePath):
    print("File Not Found! Please enter correct path and filename")
    imagePath = input("Enter image path: ")

pieces = int(input("Enter N to cut the image into NxN pieces: "))
while pieces < 2:
    print("Invalid input! N must be greater than 1")
    pieces = int(input("Enter N to cut the image into NxN pieces: "))

for i in range(pieces):
    for j in range(pieces):
        order.append([i,j])

ogOrder = order.copy()

rnd.shuffle(order)

img = cv2.imread(imagePath)

#height = np.array(img).shape[0] ; width = np.array(img).shape[1]
h = np.array(img).shape[0]
w = np.array(img).shape[1]

#generating bg black image
#bg[startH:endH ,startW:endW, :]
#bg[10:(h//3)+10,10:(w//3)+10:] = img[0:(h//3),0:(w//3):]
bg = np.zeros((h+(pieces*10+10), w+(pieces*10+10), 3), np.uint8)

#to iterate through order list
n = 0
    
for k in range(pieces):
    for l in range(pieces):
        i = order[n][0]
        j = order[n][1]
        
        bg[(h//pieces*k)+10*(k+1) : ((h//pieces)*(k+1))+10*(k+1) , (w//pieces*l)+10*(l+1):((w//pieces)*(l+1))+10*(l+1), :] = img[(h//pieces)*i:((h//pieces)*(i+1)) , (w//pieces)*j:((w//pieces)*(j+1)), :]
        
        n = n + 1

cv2.imshow("Shuffled Image", bg)

#creating white bg image
wbg = np.ones((h, w, 3), np.uint8)
wbg.fill(255)

currentOrder = order.copy()

print("\nIndex 1 is the piece that you want to select from the \"Shuffled Image\"\nAnd, Index 2 where you want to put that on the Board\n")
while 1:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    index1 = int(input("Enter Index 1: "))
    
    while index1 > (pieces*pieces) or index1 < 1:
        print("Invalid input! Input must be between 1 and",(pieces*pieces))
        index1 = int(input("Enter Index 1: "))

    index1 = index1 - 1
    
    index2 = int(input("Enter Index 2: "))
    
    while index2 > (pieces*pieces) or index2 < 1:
        print("Invalid input! Input must be between 1 and",(pieces*pieces))
        index2 = int(input("Enter Index 2: "))
        
    index2 = index2 - 1
    
    wbg[(h//pieces*ogOrder[index2][0]) : ((h//pieces)*(ogOrder[index2][0]+1)) , (w//pieces*ogOrder[index2][1]):((w//pieces)*(ogOrder[index2][1]+1)), :] = img[(h//pieces)*order[index1][0]:((h//pieces)*(order[index1][0]+1)) , (w//pieces)*order[index1][1]:((w//pieces)*(order[index1][1]+1)), :]
    
    currentOrder[index2] = order[index1]
    
    if np.array_equal(np.array(currentOrder),np.array(ogOrder)):
        cv2.destroyAllWindows()
        cv2.imshow("Puzzle Solved", wbg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Done")
        break
    cv2.imshow("Image", wbg)
cv2.destroyAllWindows()