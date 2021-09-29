import cv2 as cv
import numpy as np

#0 for system cam, 1 for external cam or provide video path 
video = cv.VideoCapture(0) 


#video not accessable
if(video.isOpened() == False):
    print('Video path not satisfied')


#checking if ther video is readable or not
while(video.isOpened()):
    ret, frame = video.read()

    if ret == True:
        #using haar cascade to deteect faces
        #provide the path to your cascade classifier
        face = cv.CascadeClassifier('training files/faceTraining/classifier/cascade.xml') 

        frame=cv.flip(frame, 1)

        #detecting faces
        faces = face.detectMultiScale(frame, 2, 2)

        #marking the faces
        for (x, y, w, h) in faces:
            frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)
            frame = cv.putText(frame, 'Face', (x+3, y+13), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        #displayig each Frame
        cv.imshow('Face', frame)    


        k = cv.waitKey(1) & 0xFF
        #press esc to exit
        if k == 27:
            break
    else:
        break

cv.destroyAllWindows()
