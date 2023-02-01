#Kaushik&Kishan File
import cv2 
import numpy as np
import imutils
import sys
import pytesseract
import pandas as pd
import time

#to take camera input
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()

        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='D:\Temp Files\Vehicle-Number-Plate-Reading\carz.jpeg', img=frame)
            # cv2.imwrite(filename='carz.jpeg', img=frame)
            cv2.imshow
            webcam.release()

            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")

        
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

