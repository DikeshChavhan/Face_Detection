#import cv2
#video_capture = cv2.VideoCapture(0)
#while True:
#    ret, frame = video_capture.read()
#    if not ret:
#        break
#    cv2.imshow('Video', frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#video_capture.release()
#cv2.destroyAllWindows()
# This code captures video from the webcam and displays it in a window.



import cv2
face_cap = cv2.CascadeClassifier("C:/Users/Dikesh Chavhan/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_alt_tree.xml")
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    col = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows() 