import cv2
import numpy as np
from skimage.transform import resize

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
frame = cv2.resize(frame, (0, 0), fx=1.2, fy=1.2)
cv2.imwrite("picture.jpg", frame)