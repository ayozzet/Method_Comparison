import cv2
import numpy as np

cap = cv2.VideoCapture('videoplayback(360p).mp4')

while True:

    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #mandatory
    blur = cv2.medianBlur(frame,5)
    pts = np.array([[220,240],[419,240],[639,330],[639,0],[0,0],[0,330]], np.int32)
    roi = cv2.fillPoly(blur,[pts],(0,0,0))

    mask = cv2.inRange(blur, roi, roi)
    display = cv2.bitwise_and(blur, frame, mask = mask)

    th1 = cv2.adaptiveThreshold(display,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    trim_edge = np.array([[220,240],[419,240],[639,330],[639,0],[0,0],[0,330]], np.int32)
    trim_edge = pts.reshape((-1,1,2))
    cv2.polylines(th1,[trim_edge],True,(0,0,0),1)

    cv2.imshow('Original',th1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
