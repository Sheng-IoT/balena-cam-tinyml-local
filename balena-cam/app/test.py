#!/usr/bin/env python3

import cv2

cap = cv2.VideoCapture("./test.h264")

# Capture frame
ret, frame = cap.read()
if ret:
    cv2.imwrite('./image.jpg', frame)
    print("captured")
else:
    print("failed")

cap.release()
