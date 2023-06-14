import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kozlo\PycharmProjects\OpenCV\OpenCV\images\astronaut.jpg")

# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Конвертація у контрастні кольори лишається 1 шар з 3.
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # Конвертація у біль тусклих кольорах, також лишається 1 шар.
# img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)  # Зворотня конвертація до формату BGR
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Конвертація з BGR у RGB для корректного відображення іншими бібліотеками


# Розбиває на шари відповідно до кольорового формату об'єкта. Кожен шар залишається у ЧБ форматі, але концепція така,
# що всі кольори вказанної гами r, g або b трансформуються у білі точки по мірі їх насиченню відповідним кольором.
b, g, r = cv2.split(img)

# Зворотньо збирає з розбитих шарів. Метод merge приймає множину з шарами.
img = cv2.merge((b, g, r))


cv2.imshow("Result", img)
cv2.waitKey(0)