import numpy as np
import cv
import cv2
import time

cap = cv2.VideoCapture(0)
# Supported
# 1280 x 1024
# 352 x 288
# 800x600 

cap.set(3, 352)
cap.set(4, 288)
time.sleep(1)

# Set the window to fullscreen
cv2.namedWindow('frame', cv.CV_WINDOW_NORMAL)
cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN) 

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
