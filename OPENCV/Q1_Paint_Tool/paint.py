import cv2
import numpy as np

draw = False
window_name = "Canvas"

img1 = np.zeros((695, 615, 3), np.uint8)
img1[:] = 225, 225, 225


def nothing(x):
    pass


def draw_circle(event, x, y, flags, param):
    global draw, window_name, img1

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.circle(img1, (x, y), cv2.getTrackbarPos("Brush Size", 'paint'),
                       (cv2.getTrackbarPos("B", 'paint'),
                        cv2.getTrackbarPos("G", 'paint'),
                        cv2.getTrackbarPos("R", 'paint')),
                       -1)

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.circle(img1, (x, y), cv2.getTrackbarPos("Brush Size", 'paint'),
                   (cv2.getTrackbarPos("B", 'paint'),
                    cv2.getTrackbarPos("G", 'paint'),
                    cv2.getTrackbarPos("R", 'paint')),
                   -1)


def eraser(event, x, y, flags, param):
    global draw, window_name, img1

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.circle(img1, (x, y), cv2.getTrackbarPos("Eraser Size", 'paint'),
                       (225,225,225), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.circle(img1, (x, y), cv2.getTrackbarPos("Eraser", 'paint'),
                   (225,225,225), -1)


# Create a black paint, a window
img = np.zeros((250, 512, 3), np.uint8)
cv2.namedWindow('paint')
# create trackbars for color change
cv2.createTrackbar('R', 'paint', 0, 255, nothing)
cv2.createTrackbar('G', 'paint', 0, 255, nothing)
cv2.createTrackbar('B', 'paint', 0, 255, nothing)
cv2.createTrackbar("Brush Size", 'paint', 1, 8, nothing)
cv2.createTrackbar("Eraser", 'paint', 0, 1, nothing)
cv2.createTrackbar("Eraser Size", 'paint', 1, 8, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'paint', 0, 1, nothing)

while 1:

    cv2.imshow('paint', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'paint')
    g = cv2.getTrackbarPos('G', 'paint')
    b = cv2.getTrackbarPos('B', 'paint')
    s = cv2.getTrackbarPos(switch, 'paint')
    er = cv2.getTrackbarPos("Eraser", 'paint')

    if s == 0:
        img[:] = 0
    else:

        cv2.namedWindow(window_name)

        cv2.imshow(window_name, img1)
        img[:] = [b, g, r]
        cv2.setMouseCallback(window_name, draw_circle)

        if er == 1:
            cv2.setMouseCallback(window_name, eraser)

cv2.destroyAllWindows()