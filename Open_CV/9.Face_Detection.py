import cv2

#Haar cascades are XML files that can be used in OpenCV to detect specified objects.
#How to create Cascades Files?

faceCascade = cv2.CascadeClassifier("/Users/devmbandhiya/Desktop/Open_CV/Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("/Users/devmbandhiya/Desktop/Open_CV/Resources/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4) #min neighbors is 4

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 5)

cv2.imshow("Result", img)
cv2.waitKey(0)