import numpy as np
import cv2 as cv

img = cv.imread("Images/dog.jpg")
cv.imshow("Image",img)
cv.waitKey(0) # waits until a key is pressed
cv.destroyAllWindows() # destroys the window showing image