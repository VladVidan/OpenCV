import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype="uint8")

# RGB - прийнятий формат кольорів , але в OpenCV він назівається BGR!
# photo[100:150, 200:280] = 214, 39, 182

# 1 кортеж - піксель з якого рисується фігура
# 2 кортеж - розмір фігури
# 3 кортеж - BGR палітра кольору контурів фігури
# 4 кортеж - кількість пікселів товщини контурів фігури. Або "cv2.FILLED" для повної заливки.
cv2.rectangle(photo, (140, 150), (100, 100), (214, 39, 182), thickness=cv2.FILLED)

# Схожий принцип з малюванням ліній.
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (214, 39, 182), thickness=3)

# З кругом , аргументи - 1.Обьект, 2.Центр круга, 3.Радіус, 4.Колір, 5.Товщина лінії в пікс, або таж сама заливка.
cv2.circle(photo, (photo.shape[0] // 2, photo.shape[1] // 2), 150, (214, 39, 182), thickness=1)


# Метод відображення тексту
# 1 аргумент - об'єкт зображення
# 2 - Зміст тексту
# 3 - Висота та довжина поля тексту
# 4 - Шрифт тексту
# 5 - Одиниця розміру (стандарт - 1)
# 6 - BGR колір
# 7 - Товщина полос у пікселях
cv2.putText(photo, "VidanProject", (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Photo", photo)
cv2.waitKey(0)

