
from tkinter import *
from PIL import Image, ImageTk
import cv2, os, sys, pickle
import time
import numpy as np
from configs import *
import random





faceCascade = cv2.CascadeClassifier('bin/haarcascade_frontalface_default.xml')
profileCascade = cv2.CascadeClassifier('bin/haarcascade_profileface.xml')

recognizer = cv2.face_LBPHFaceRecognizer.create()

recognizer.read('face_rec_saved_model.yaml')

with open(label_name_map_file, 'rb') as handle:
        label_name_map = pickle.load(handle)

print("Press 'q' to quit\n\n\n")
video_capture = cv2.VideoCapture(0)

def predictFacesFromWebcam(label2name_map):
        video_capture = cv2.VideoCapture(0)
        i=0
        global d
        e=0
        while e==0:
                
                ret, frame = video_capture.read()
                print(ret)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, scaleFactor, minNeighbors, cascadeFlags, minSize)
                for (x, y, w, h) in faces:
                       
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        name_predicted, confidence = recognizer.predict(cv2.resize(gray[y: y + h, x: x + w], face_resolution))
                        print(str(name_predicted) +' , ' +str(confidence))
                        if(name_predicted!=0 and confidence<confidence_threshold):
                                print("It is predicted as "+label2name_map[name_predicted])
                                cv2.putText(frame, label2name_map[name_predicted], (x+3,y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
                                
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        print("\nQuitting")
                        break
        video_capture.release()
        cv2.destroyAllWindows()
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
   
   
    if username1=="admin" and password1=="1234":
         predictFacesFromWebcam(label_name_map)
                
    else:
        
        password_not_recognised()
        time.sleep(1)

def send_message(d,num):
        import requests

        url = "https://www.fast2sms.com/dev/bulkV2"

        querystring = {"authorization":"zNVnDvTOWoPyud5w8f20sQUrZjKcJiBeHa3GCq16I7XmAYglpE0Aas9lQHyfObBdkM8KVSEcTZoD2Yz7","variables_values":str(d),"route":"otp","numbers":str(num)}

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
def mess():
    send_message(otp,"9894938971")
def login():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("766x708")
    login_screen.configure(background='#f5f5f5')
    Label(login_screen, text="Please enter details below to login",bg="#051094", font=("Calibri", 30)).place(x=150,y=10)
   
    
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="USERNAME",font=("Verdana", 15),bg="#c6eb73",fg="black").place(x=320,y=200)
    username_login_entry = Entry(login_screen,justify=RIGHT, textvariable=username_verify,font=('Verdana',15,'bold')).place(x=250,y=240)
    Label(login_screen, text="PASSWORD ",font=("Verdana", 15),bg="#c6eb73",fg="black").place(x=320,y=300)
    password_login_entry = Entry(login_screen, justify=RIGHT,textvariable=password_verify, show= '*',font=('Verdana',15,'bold')).place(x=250,y=340)
    Button(login_screen, text="Login", width=30, height=2,bd=5, command = login_verify,bg="#a6ed07",activebackground="#c6eb73").place(x=270,y=400)
def main_account_screen():
    login()
   
    login_screen.mainloop()
          
         
 
main_account_screen()
