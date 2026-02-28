import cv2

img = cv2.imread("dog.jpg")
cv2.imshow("Original Image", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)
small = cv2.resize(img, (300,300))
cv2.imshow("Resized Image", small)
cv2.waitKey(0)
cv2.destroyAllWindows()