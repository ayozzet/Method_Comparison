import cv2
import numpy as np
import logging

def roi(img,vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask,vertices,255)
    masked_image=cv2.bitwise_and(img,mask)
    return masked_image

def preprocess(img):
    height = img.shape[0]
    width = img.shape[1]
    #roi_vertices = [(0,height),(5*width/10,6*height/10),(width,height)]
    roi_vertices = [(0,height),(5*width/10,3*height/4),(width,height)]
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray,100,150)
    cropped = roi(canny,np.array([roi_vertices],np.int32))
    return cropped

def draw_hough_lines(img,lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(255,0,255),thickness=2)
    img = cv2.addWeighted(img,0.8,blank_image,1,0.0)
    return img

lgr = logging.getLogger('Time taken')
lgr.setLevel(logging.DEBUG)
fh = logging.FileHandler('Time_HoughLines.csv')
fh.setLevel(logging.DEBUG)
frmt = logging.Formatter('%(message)s')
fh.setFormatter(frmt)
lgr.addHandler(fh)

cap = cv2.VideoCapture('videoplayback(360p).mp4')
while True:
    e1 = cv2.getTickCount()
    ret,frame = cap.read()
    cropped= preprocess(frame)
    lines = cv2.HoughLinesP(cropped,rho=2,threshold=20,theta=np.pi/180,minLineLength=10,maxLineGap=30,lines=np.array([]))
    img = draw_hough_lines(frame,lines)
    cv2.imshow('Lane detection',img)

    e2 = cv2.getTickCount()
    time = (e2-e1)/cv2.getTickFrequency()
    print(time)
    lgr.info(time)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()
