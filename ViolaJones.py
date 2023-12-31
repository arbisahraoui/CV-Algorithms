import cv2
import numpy as np

SCALEFACTOR = 1.1
MINNEIGHBORS = 2
FLAGS = 0 | cv2.CASCADE_SCALE_IMAGE
MINSIZE = (30, 30)

COLOR_FRONT = (255,0,255)
COLOR_PROFILE = (255,0,0)

face_cascade_front_path = './haarcascade_frontalface_alt2.xml'
face_cascade_profile_path = './haarcascade_profileface.xml'

minecraft_image = cv2.imread('../material/test.png')

cap = cv2.VideoCapture(0)

casc_front = cv2.CascadeClassifier()
casc_front.load(face_cascade_front_path)

casc_profile = cv2.CascadeClassifier()
casc_profile.load(face_cascade_profile_path)

while cap.isOpened():
    ret, frame = cap.read()
    #frame = resize(frame, 0.4)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    detected = casc_front.detectMultiScale(frame_gray, SCALEFACTOR, MINNEIGHBORS, FLAGS, MINSIZE)
    detected_profile = casc_profile.detectMultiScale(frame_gray, SCALEFACTOR, MINNEIGHBORS, FLAGS, MINSIZE)

    for (x,y,w,h) in detected:
        cv2.rectangle(frame, (x, y),(x + w, y + h), COLOR_FRONT, 3)

    for (x,y,w,h) in detected_profile:
        cv2.rectangle(frame, (x, y),(x + w, y + h), COLOR_PROFILE, 3)


    cv2.imshow("video", frame)
    if cv2.waitKey(1) == ord('q'):
        break
