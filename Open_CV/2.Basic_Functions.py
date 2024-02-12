import cv2
import numpy as np
 
img = cv2.imread("/Users/devmbandhiya/Desktop/Projects/Open_CV/Resources/lena.png")
kernel = np.ones((5,5),np.uint8)   #will be used in dilation and erosion operations
 
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #Conersion BGR2RGB, BGR2GRAY, GRAY2BGR, RGB2BGR
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)      #Kernel Size and Standard Deviation
imgCanny = cv2.Canny(img,150,200)                 #Lower and Upper Thresholds for for Edge Detection
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
 
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)
