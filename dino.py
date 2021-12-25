# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 04:12:21 2021

@author: PankK
"""
import cv2
import numpy as np
from mss import mss
from PIL import Image
import time
import skimage
from skimage import filters
import pyautogui as pt
import matplotlib.pyplot as plt

def processing(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    
    
    thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    print(thresh)
    return thresh

def get_screen():
    get_img = mss()
    
    
    while(True):
        
        img = get_img.grab(area)
       
        img = np.array(img)
       # print(img[0])
        cv2.imwrite("this.png", img)
        thresh = processing(img)
        
        mean = np.mean(thresh)
        
        print("mean ", mean[0,:])
        
        if float(50) in mean:
            pt.press('space')
        ch = cv2.waitKey(5)
        if ch == ord("q"):
            cv2.destroyAllWindows()
            break
 
time.sleep(6)
area = {"top":310 , "left": 600, "width": 70, "height": 140}    
get_screen()