import cv2
cap = cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("capture.jpg", frame)
        break
cap.release()
cv2.destroyAllWindows()