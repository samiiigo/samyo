import cv2
face_cascade = cv2.CascadeClassifier('smile detet/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('smile detet/haarcascade_smile.xml')


cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    cv2.imshow('lcam star',frame)
    if cv2.waitKey(10) == ord('q'):
        break