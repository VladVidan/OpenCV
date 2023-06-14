import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kozlo\PycharmProjects\OpenCV\OpenCV\images\astronaut.jpg")

new_img = np.zeros(img.shape, dtype="uint8")


# img = cv2.flip(img, 1) # Відзеркалює зображення по гор. та верт.


def rotate(img_param, angle):
    """Функція для развороту зображення."""
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)  # Створення матриці
    return cv2.warpAffine(img_param, mat, (width, height))


def transform(img_param, x, y):
    """Функція зміщення зображення у своїх рамкаї. Створює чорні контури."""
    mat = np.float32([[1, 0, x], [0, 1, y]]) # Координати зміщення
    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))


# img = transform(img, 30, 200)

# img = rotate(img, 90)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Переводимо в сірій
img = cv2.GaussianBlur(img, (5, 5), 0)  # Додаємо блюр
img = cv2.Canny(img, 100, 140)  # Діапазон пошуку по BGR(0-255). Задано не меньш ніж 100 та не більше ніж 140

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # Отримуємо список координат зображення.

# Фарбує отримані контури за вказанним кольором.
cv2.drawContours(new_img, con, -1, (230, 111, 148), 1)

print(con)

cv2.imshow("Result", img)

cv2.waitKey(0)
