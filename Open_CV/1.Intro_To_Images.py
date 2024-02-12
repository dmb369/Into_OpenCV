import cv2

#Read Images

# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("/Users/devmbandhiya/Desktop/Projects/Open_CV/Resources/lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg",img)
# Wait for a key press (0 means wait indefinitely)
cv2.waitKey(0)


#Read Video
frameWidth = 640
frameHeight = 640
cap = cv2.VideoCapture("/Users/devmbandhiya/Desktop/Projects/Open_CV/Resources/test_video.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameHeight, frameWidth))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #The bitwise AND (& 0xFF) is used to mask off the extra bits that are returned.
        break

#Read VideoCam
import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)          #property identifiers
cap.set(4, frameHeight)
cap.set(10, 150)                #sets the brightness of the VideoCam
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





