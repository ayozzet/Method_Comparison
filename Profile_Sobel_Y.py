import cv2
import numpy as np
import logging

lgr = logging.getLogger('Time taken')
lgr.setLevel(logging.DEBUG)
fh = logging.FileHandler('Time_taken_SobelY.csv')
fh.setLevel(logging.DEBUG)
frmt = logging.Formatter('%(message)s')
fh.setFormatter(frmt)
lgr.addHandler(fh)

cap = cv2.VideoCapture('videoplayback(360p).mp4')

while True:
    e1 = cv2.getTickCount()
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pts = np.array([[220,240],[419,240],[639,330],[639,0],[0,0],[0,330]], np.int32)
    roi = cv2.fillPoly(gray,[pts],(0,0,0))

    mask = cv2.inRange(gray, roi, roi)
    display = cv2.bitwise_and(gray, gray, mask = mask)
    # Calculation of Sobely
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)

    trim_edge = np.array([[220,240],[419,240],[639,330],[639,0],[0,0],[0,330]], np.int32)
    trim_edge = pts.reshape((-1,1,2))
    cv2.polylines(sobely,[trim_edge],True,(0,0,0),2)

    cv2.imshow('Original',sobely)
    e2 = cv2.getTickCount()
    time = (e2-e1)/cv2.getTickFrequency()
    print(time)
    lgr.info(time)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
