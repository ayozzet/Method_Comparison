import cv2
import numpy as np

#cap = cv2.VideoCapture('videoplayback(720p).mp4')
cap = cv2.VideoCapture('videoplayback(360p).mp4')
#roi = cv2.selectROI(cap)

while True:
    ret, frame = cap.read()
    edge = cv2.Canny(frame, 100, 200)
    print(edge.shape)
    cv2.imshow('Original',edge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
