import numpy as np
import math
from os.path import exists
from PIL import Image

# crop function
def crop(image, dist1, dist2, dist3, dist4):
    ogImg = Image.open(image)
    
    ogImg = np.array(ogImg,"uint8")
    
    ogImg = ogImg[dist1:ogImg.shape[1]-dist3, dist4:ogImg.shape[0]-dist2]
    
    image = Image.fromarray(ogImg)
    image.show()
    image = image.save("cropped.jpg")

# blending function
def blending(img1, img2, weight1, weight2, gamma):
    x1 = np.array(Image.open(img1))
    x2 = np.array(Image.open(img2))
    
    image = x1*weight1+x2*weight2+gamma

    image = image.astype("uint8")
    
    image = Image.fromarray(image)
    image.show()
    image = image.save("blend.jpg")

# rotate function
def rotate(image, direction, angle):
    ogImg = Image.open(image)

    x = np.array(ogImg)

    if angle == 180:
        x[:, :, :] = x[::-1]
    else:
        b = x[:, :, 0]
        g = x[:, :, 1]
        r = x[:, :, 2]

        x = np.stack((b.T, g.T, r.T), axis=-1)

        if direction == "c" or direction == "C":
            x = x[:, ::-1, :]

    image = Image.fromarray(x)
    image.show()
    image = image.save("rotate.jpg")

# brightness manipulation function
def bright_manipulate(image, brightness):
    ogImg = Image.open(image)
    
    brightness = brightness/100.0

    x = np.array(ogImg)

    x = x*brightness
    x = x.astype("uint8")
    
    image = Image.fromarray(x)
    image.show()
    image = image.save("bright.jpg")

# rotate at angle
def rotate_at_angle(image, direction, angle):
    ogImg = Image.open(image)
    ogImg = np.array(ogImg)
    
    if direction == "c" or direction == "C":
        angle = 360 - angle

    # Define the most occuring variables
    angle=math.radians(angle)
    cosine=math.cos(angle)
    sine=math.sin(angle)
    height=ogImg.shape[0]
    width=ogImg.shape[1]
    
    # Define the height and width of the new ogImg that is to be formed
    new_height  = round(abs(ogImg.shape[0]*cosine)+abs(ogImg.shape[1]*sine))+1
    new_width  = round(abs(ogImg.shape[1]*cosine)+abs(ogImg.shape[0]*sine))+1
    
    # define another ogImg variable of dimensions of new_height and new _column filled with zeros
    output=np.zeros((new_height,new_width,ogImg.shape[2]))
    
    # Find the centre of the ogImg about which we have to rotate the ogImg
    original_centre_height   = round(((ogImg.shape[0]+1)/2)-1)
    original_centre_width    = round(((ogImg.shape[1]+1)/2)-1)
    
    # Find the centre of the new ogImg that will be obtained
    new_centre_height= round(((new_height+1)/2)-1)
    new_centre_width= round(((new_width+1)/2)-1)

    for i in range(height):
        for j in range(width):
            #co-ordinates of pixel with respect to the centre of original ogImg
            y=ogImg.shape[0]-1-i-original_centre_height                   
            x=ogImg.shape[1]-1-j-original_centre_width                      
    
            #co-ordinate of pixel with respect to the rotated ogImg
            new_y=round(-x*sine+y*cosine)
            new_x=round(x*cosine+y*sine)
            new_y=new_centre_height-new_y
            new_x=new_centre_width-new_x
    
            # adding if check to prevent any errors in the processing
            if 0 <= new_x < new_width and 0 <= new_y < new_height and new_x>=0 and new_y>=0:
                output[new_y,new_x,:]=ogImg[i,j,:]
    
    output = output.astype("uint8")
    image = Image.fromarray(output)
    image.show()
    image = image.save("rotate_angle.png")


# main program
print(" ____________________________________")
print("| Welcome to BugBusters Image Editor |")
print(" ````````````````````````````````````")
print("Enter choice to execute one of the following functions:")
print("[1] Crop")
print("[2] Blending")
print("[3] Rotation")
print("[4] Brightness Manipulation")
print("[5] Rotate at angle")
print("[*] Any other key to Quit")

choice = input("Enter choice: ")

if choice == "1":
    path = input("[1]Enter path to image: ")
    while not exists(path):
        print("File Not Found. Please enter correct path and filename.")
        path = input("[1]Enter path to image: ")
    crop(path, int(input("Enter distance 1: ")), int(input("Enter distance 2: ")), int(
        input("Enter distance 3: ")), int(input("Enter distance 4: ")))

elif choice == "2":
    path1 = input("[2]Enter path to image 1: ")
    while not exists(path1):
        print("File Not Found. Please enter correct path and filename.")
        path1 = input("[2]Enter path to image 1: ")
    path2 = input("[2]Enter path to image 2: ")
    while not exists(path2):
        print("File Not Found. Please enter correct path and filename.")
        path2 = input("[2]Enter path to image 2: ")
    blending(path1, path2, float(input("Enter weight 1: ")), float(
        input("Enter weight 2: ")), int(input("Enter gamma: ")))

elif choice == "3":
    path = input("[3]Enter path to image: ")
    while not exists(path):
        print("File Not Found. Please enter correct path and filename.")
        path = input("[3]Enter path to image: ")
    rotate(path, input("[3]Enter direction clockwise(C) or anticlockwise(A): "), int(
        input("Enter angle: ")))

elif choice == "4":
    path = input("[4]Enter path to image: ")
    while not exists(path):
        print("File Not Found. Please enter correct path and filename.")
        path = input("[4]Enter path to image: ")
    bright_manipulate(path, int(input("Enter brightness %: ")))

elif choice == "5":
    path = input("[5]Enter path to image: ")
    while not exists(path):
        print("File Not Found. Please enter correct path and filename.")
        path = input("[5]Enter path to image: ")
    rotate_at_angle(path, input(
        "[5]Enter direction clockwise(C) or anticlockwise(A): "), int(input("Enter angle: ")))
else:
    print("Quit")
