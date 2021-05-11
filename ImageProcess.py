
#import python neccessary python libraries
from __future__ import print_function
from imutils.object_detection import non_max_suppression
import numpy as np
import imutils
import PerformanceTest
from PIL import Image
import cv2
import time
import os

#Initialize the hog descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#1280x720

#take picture
os.system('fswebcam -r 320x240 -S 3 --jpeg 50 --no-banner --save /home/pi/App/New/Python2/images/CapturedImage.jpg')


#Initialize the face_cascade
face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades_cuda/haarcascade_frontalface_alt2.xml')


def detect():
    start_time = time.time()

    #Crop the image and save
    #image = 'FYP_Images/CapturedImage.jpg'
    #img = Image.open(image)
    #area = (x,y,h,w)
    #cropedimage = img.crop(area)
    #cropedimage.save("FYP_Images/ProcessImage.jpg")
    
    #resize
    image = 'FYP_Images/ProcessImage.jpg'
    image = cv2.imread(image)
    #cv2.imshow("cropped Image", image)
    image = imutils.resize(image, width=min(300, image.shape[1]))
    #cv2.imshow("Resized Image", image)

    #human body detection
    (bodies, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

    #face detection    
    faces = face_cascade.detectMultiScale(image, 1.1, 2)

    start_draw = time.time()
    
    #Draw rectangles around the faces detected
    for i in range (len(faces)):
        cv2.rectangle(image,(faces[i][0],faces[i][1]),(faces[i][0]+faces[i][2],faces[i][1]+faces[i][3]),(255,0,0),2)

    #Make an array with the start and end points of the rectangles around the bodies 
    for i in range (len(bodies)):
         bodies[i] = np.array([bodies[i][0], bodies[i][1],bodies[i][0]+bodies[i][2], bodies[i][1]+bodies[i][3]])

    #Performance Testing
    draw_Taken = time.time() - start_draw
    draw_TakenMs = round(draw_Taken * 1000 , 1)
    PerformanceTest.setDrawRectangleTime(draw_TakenMs)

    #Remove overlaping body rectangles
    pickBodies = non_max_suppression(bodies, probs=None, overlapThresh=0.65)

    #Draw rectangles around the bodies correctly identified
    
    body= len(pickBodies)
    face= len(faces)
    people= body + face

    for i in range (len(pickBodies)):
        cv2.rectangle(image, (pickBodies[i][0], pickBodies[i][1]), (pickBodies[i][2], pickBodies[i][3]), (0, 255, 0), 2)
        
        if ((body != 0) or (face != 0)):  
            for j in range (len(faces)):
                if (pickBodies[i][2]>(faces[j][0]+faces[j][2]) and pickBodies[i][0]<faces[j][0] and pickBodies[i][1]<faces[j][1] and pickBodies[i][2]>faces[j][2] and pickBodies[i][3]>faces[j][3]):
                    people= people-1

    #Performance Testing
    timeTaken = time.time() - start_time
    timeTakenMs = round(timeTaken * 1000 , 1)
    PerformanceTest.setImageProcessTime(timeTakenMs)
    
    #Show an image with the rectangles drawn
    cv2.imshow("Result", image)
    cv2.waitKey(100)
    cv2.destroyAllWindows()

#Print the No. of Bodies and the No. of Faces
    print('Number of peoples:',people)
    return people
#Call the detect function
#detect()
