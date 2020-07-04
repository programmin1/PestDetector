import numpy as np
import cv2
from matplotlib import pyplot as plt
import pylab

from scipy import ndimage
import os

for img in os.listdir('.'):
    if img.endswith('.jpg'):
        image = cv2.imread(img)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.resize(gray_image, (int(gray_image.shape[1]/2), int(gray_image.shape[0]/2) ))
        ret, threshimg = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY)
        cv2.imshow('opening',threshimg)
        objects = ndimage.find_objects(threshimg)
        for ob in objects:
            print(ob)
        cv2.waitKey(0)                 # Waits forever for user to press any key   
        cv2.destroyAllWindows()
