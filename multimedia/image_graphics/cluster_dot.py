import cv2
import numpy as np
img = cv2.imread("dog.jpg", 0)

rows, cols = img.shape

for i in range(0, rows-1, 2):
    for j in range(0, cols-1, 2):
        block = img[i:i+2, j:j+2]
        avg = np.mean(block)

        if avg > 128:
            img[i:i+2, j:j+2] = 255
        else:
            img[i:i+2, j:j+2] = 0

cv2.imshow("Dithered Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()