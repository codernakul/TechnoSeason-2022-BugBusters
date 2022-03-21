#import numpy as np
import cv2
from os.path import exists

def crop(image, dist1, dist2, dist3, dist4):
    ogImg = cv2.imread(image)
    cv2.imshow("Og. Image",ogImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(ogImg.shape[1],ogImg.shape[0])
    ogImg = ogImg[dist1:ogImg.shape[1]-dist3, dist4:ogImg.shape[0]-dist2, :]
    cv2.imwrite('Images\cropped.png',ogImg)
    cv2.imshow("Cropped Image",ogImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def bright_manipulate(image, brightness):
    ogImg = cv2.imread(image)
print(" ____________________________________")
print("| Welcome to BugBusters Image Editor |")
print(" ````````````````````````````````````")
print("Enter choice to execute one of the following functions:")
print("[1] Crop")
print("[2] Blending")
print("[3] Rotation")
print("[4] Brightness Manipulation")
choice = input("Enter choice: ")
if choice == "1":
    path = input("Enter path to image: ")
    if not exists(path):
        print("File Not Found")
        path = input("Enter path to image: ")
    crop(path,int(input("Enter distance 1: ")),int(input("Enter distance 2: ")),int(input("Enter distance 3: ")),int(input("Enter distance 4: ")))
# elif choice == "2":

# elif choice == "3":
    # path = input("Enter path to image: ")
    # if not exists(path):
        # print("File Not Found")
        # path = input("Enter path to image: ")
    # print("done")

# elif choice == "4":

else:
    print("Quit")