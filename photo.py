import cv2, os, sys, time
import numpy as np
from PIL import Image
from configs import *

i=0

video_capture = cv2.VideoCapture(0) #Set the source webcam
video_capture .set(3,640)
video_capture .set(4,480)
print("Enter 'c' to capture the photo\n")
print("Enter 'q' to quit..\n\n")
print("Waiting to capture photo......\n\n")

while True:
        n = input("Enter: ")
        if(n=='q'):
                print("Quitting..")
                break
        if(n=='c'):
                name = input("Enter name: ")
                neram = str(int(time.time()))
                while i<30:
                        ret, frame = video_capture.read()
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        cv2.imshow('Video', gray)
                        if cv2.waitKey(1) & 0xFF == ord('n'):
                                cv2.imwrite(db_path+"/"+str(name)+"."+neram+str(i)+".png", gray)
                                print("Saved as "+str(name)+"."+neram+str(i)+".png"+"\n\n")
                                i+=1
                print("Waiting to capture photo......")

print("\n\nPROCESS STOPPED......")
video_capture.release()
