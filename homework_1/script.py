import cv2

camera = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 2, 7, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    eyes = eye_cascade.detectMultiScale(gray, 1.2, 7, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 245, 67), 2)

    cv2.imshow("Detector de fete si ochisori frumosi xD", frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
