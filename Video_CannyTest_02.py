import cv2
import numpy as np

#cap = cv2.VideoCapture('videoplayback(720p).mp4')
cap = cv2.VideoCapture('videoplayback(360p).mp4')

while True:
    ret, frame = cap.read()
    pts = np.array([[220,240],[419,240],[639,330],[639,0],[0,0],[0,330]], np.int32)
    roi = cv2.fillPoly(frame,[pts],(0,0,0))

    mask = cv2.inRange(frame, roi, roi)
    display = cv2.bitwise_and(frame, frame, mask = mask)
    edge = cv2.Canny(display, 100, 200)
    trim_edge = np.array([[220,240],[419,240],[639,330],[639,0],[0,0],[0,330]], np.int32)
    trim_edge = pts.reshape((-1,1,2))
    cv2.polylines(edge,[trim_edge],True,(0,0,0),2)

    print(edge.shape)
    cv2.imshow('Original',edge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
