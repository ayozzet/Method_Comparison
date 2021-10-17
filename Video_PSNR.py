#this is just a test to find peak signal to noise ratio in image

import numpy as np
import cv2
from skimage import data, filters

# Open Video
cap = cv2.VideoCapture('videoplayback(360p).mp4')

# Randomly select 25 frames
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)

# Store selected frames in an array
frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

# Calculate the median along the time axis
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
print (medianFrame)
# Display median frame
cv2.imshow('frame', medianFrame)
cv2.waitKey(0)
