import cv2
import matplotlib.pyplot as plt

img = cv2.imread("dog.jpg", 0)  
plt.imshow(img, cmap='gray')
plt.title("Grayscale Image")
plt.show()
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.title("Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()