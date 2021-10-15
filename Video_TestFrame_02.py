import cv2
import numpy as np

#cap = cv2.VideoCapture('videoplayback(720p).mp4')
cap = cv2.VideoCapture('videoplayback(360p).mp4')

while True:
    ret, frame = cap.read()
    cv2.imshow('Original',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
