import cv2
import numpy as np

cap = cv2.VideoCapture('videoplayback(360p).mp4')

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculation of Sobelx
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)

    # Calculation of Sobely
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)

    # Calculation of Laplacian
    laplacian = cv2.Laplacian(gray,cv2.CV_64F)

    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('laplacian',laplacian)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
