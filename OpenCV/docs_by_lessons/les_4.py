import cv2
import numpy as np

img = cv2.imread("/home/vlad_vidan/PycharmProjects/OpenCV/OpenCV/images/astronaut.jpg")

# img = cv2.flip(img, 1) # Відзеркалює зображення по гор. та верт.


def rotate(img, angle):
    height, width = img.shape[:2]
    point = (width // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)

cv2.imshow("Result", img)

cv2.waitKey(0)