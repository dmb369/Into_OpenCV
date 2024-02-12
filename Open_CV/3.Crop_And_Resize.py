import cv2
import numpy as np

img = cv2.imread("/Users/devmbandhiya/Desktop/Open_CV/Resources/shapes.png")
print(img.shape)

imgResize = cv2.resize(img,(1000,500))  #(y,x)
print(imgResize.shape)

imgCropped = img[46:119,352:495]

#cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)