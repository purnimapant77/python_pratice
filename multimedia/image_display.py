import cv2

def show_image(path):
    img = cv2.imread(path)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

show_image("dog.jpg")