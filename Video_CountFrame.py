import cv2

cap= cv2.VideoCapture('videoplayback(360p).mp4')
#cap= cv2.VideoCapture('videoplayback(720p).mp4')
#cap= cv2.VideoCapture('Python (OpenCV) Course 01 - Read and Display Image.mp4')

totalframecount= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("The total number of frames in this video is ", totalframecount)
