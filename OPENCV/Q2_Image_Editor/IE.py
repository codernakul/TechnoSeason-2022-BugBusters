import numpy as np
import cv2

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

print(" ____________________________________")
print("| Welcome to BugBusters Image Editor |")
print(" ````````````````````````````````````")
print("Enter choice to execute one of the following functions:")
print("[1] Crop")
print("[2] Blending")
print("[3] Rotation")
print("[4] Brightness Manipulation")
path = input("Enter path to image: ")
crop(path,0,300,300,0)