import cv2

img = cv2.imread("dog.jpg")

cv2.imwrite("compressed.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 20])
print("Image Compressed")

compressed_img = cv2.imread("compressed.jpg")

cv2.imwrite("decompressed.jpg", compressed_img)
print("Image Decompressed")