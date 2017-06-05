import tesseract
import ctypes
import os
import time

import cv2
import numpy as np
import cv2.cv as cv

cap=cv2.VideoCapture(0)
x=1
while x==1:
    #BGR image feed from camera
    ret,img_frame =cap.read()
    cv2.imshow('output',img_frame)
    #cv2.imwrite("rgb.jpg",img_frame)
    #BGR to gray conversion
    img2 =cv2.cvtColor(img_frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale',img2)
         

    k=cv2.waitKey(10)
    #cheking for an esc key press
    if k==27:
        cv2.imwrite("grayscale.jpg",img2)
        break
cap.release()
cv2.destroyAllWindows()



api = tesseract.TessBaseAPI()
api.SetOutputName("outputName");

api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetPageSegMode(tesseract.PSM_AUTO)
mImgFile = "grayscale.jpg"

result = tesseract.ProcessPagesRaw(mImgFile,api)
print result


def robot(text):
    os.system("espeak ' " + text + " ' ")

robot(result)


