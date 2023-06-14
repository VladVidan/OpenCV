import cv2
import numpy as np

photo = cv2.imread(r"C:\Users\kozlo\PycharmProjects\OpenCV\OpenCV\images\astronaut.jpg")
img = np.zeros(photo.shape[:2], dtype="uint8")

circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (200, 300), 200, -1)

########################### Побітові операціі. №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
# img = cv2.bitwise_and(circle, square)  # Побітове поєднання 2 зображень за загальними "рисами"
# img = cv2.bitwise_or(circle, square)  # Повне поєднання зображень не зважаючи на загальні риси.
# img = cv2.bitwise_xor(circle, square)  # Поєднує зображення з ігноруванням співподаючих зон.
# img = cv2.bitwise_not(circle)  # Створює інверсію зображень.

img = cv2.bitwise_and(photo, photo, mask=circle)  # Створює маску для зображення(арг.1) формою переданою в mask(арг.3)

cv2.imshow("Result", img)

cv2.waitKey(0)
