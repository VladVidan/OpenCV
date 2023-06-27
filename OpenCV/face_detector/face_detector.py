import cv2

img = cv2.imread(r"C:\Users\kozlo\PycharmProjects\OpenCV\OpenCV\face_detector\images\many_people.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier("face_neuro.xml")

# scaleFactor - співвідношення розміру зображень до розмірів зображень по яких навчали модель
# minNeighbors - показник скільки шукаємих об'єктів може "детектити" поряд один з одним
results = faces.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6) # results - координати знайденого об'єкту.

for x, y, w, h in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)


cv2.imshow("Result", img)
cv2.waitKey(0)
