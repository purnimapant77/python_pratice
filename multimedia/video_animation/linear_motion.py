import cv2
import numpy as np

img = np.zeros((400,600,3), dtype=np.uint8)
for x in range(0,500,10):
    frame = img.copy()
    cv2.circle(frame, (x+50,200), 20, (255,0,0), -1)
    cv2.imshow("Linear Motion", frame)
    cv2.waitKey(50)
cv2.destroyAllWindows()