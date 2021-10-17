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
# Reset frame number to 0
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Convert background to grayscale
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)

# Loop over all frames
ret = True
while(ret):

    # Read frame
    ret, frame = cap.read()
    # Convert current frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pts = np.array([[220,240],[419,240],[639,330],[639,0],[0,0],[0,330]], np.int32)
    roi = cv2.fillPoly(frame,[pts],(0,0,0))

    mask = cv2.inRange(frame, roi, roi)
    display = cv2.bitwise_and(frame, frame, mask = mask)
    # Calculate absolute difference of current frame and
    # the median frame
    dframe = cv2.absdiff(display, grayMedianFrame)
    # Treshold to binarize
    th, dframe = cv2.threshold(dframe, 30, 255, cv2.THRESH_BINARY)

    trim_edge = np.array([[220,240],[419,240],[639,330],[639,0],[0,0],[0,330]], np.int32)
    trim_edge = pts.reshape((-1,1,2))
    cv2.polylines(dframe,[trim_edge],True,(255,255,255),2)
    print(dframe)
    # Display image
    cv2.imshow('frame', dframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video object
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
