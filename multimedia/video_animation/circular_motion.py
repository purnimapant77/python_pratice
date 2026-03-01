import cv2
import numpy as np
import math

img = np.zeros((500,500,3), dtype=np.uint8)
center_x = 250
center_y = 250
radius = 100

for angle in range(0,360,5):
    frame = img.copy()
    x = int(center_x + radius * math.cos(math.radians(angle)))
    y = int(center_y + radius * math.sin(math.radians(angle)))
    cv2.circle(frame, (x,y), 10, (0,255,0), -1)
    cv2.imshow("Circular Motion", frame)
    cv2.waitKey(50)
cv2.destroyAllWindows()