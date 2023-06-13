import cv2
import numpy as np

img = cv2.imread("../images/astronaut.jpg")

img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  # Зміна розміру

img = cv2.GaussianBlur(img, (17, 7), 0)  # Додавання блюру

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Зміна кольору.

img = cv2.Canny(img, 100, 100) # Бінарне відображеня. Чим меньша цифра - тип більше деталей.

kernel = np.ones((5, 5), np.uint8)  # Створення матриці 5х5
img = cv2.dilate(img, kernel, iterations=1)  # Розширеня "точок". Зменьшує деталізацію.
img = cv2.erode(img, kernel, iterations=1)  # Розмиває зображення, використовуючи певний структуруючий елемент.

cv2.imshow('astro', img)  # Відображення

# print(img.shape)

cv2.waitKey(0) # Час відображення. Якщо "0" - відображує до закриття.
