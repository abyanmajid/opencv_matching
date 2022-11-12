# Learning OpenCV Part 1
# Documentation: https://docs.opencv.org/

import cv2 as cv
import numpy as np

# Read image with its natural colour
img = cv.imread('img.jpg') # Base image (Set this)
object_img = cv.imread('object.PNG') # Object in image (Set this)

result = cv.matchTemplate(image=img, templ=object_img, method=cv.TM_CCOEFF_NORMED)

# Show match result on window
# cv.imshow('Result', result)
# cv.waitKey()

# Get pos of best match (MEASURED FROM TOP LEFT)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) 

print('Best match top left pos: %s' % str(max_loc)) # (x, y) coor. of best match
print('Correlation: %s' % max_val) # correlation value between object and best match in img

# Min. value for correlation to assume object is found
threshold = 0.9
if max_val >= threshold:
    print('Object was found')
    
    # get dimensions of object_img
    width = object_img.shape[1]
    height = object_img.shape[0]
    
    top_left = max_loc
    bottom_right = (top_left[0] + width, top_left[1] + height)
    
    # Draw box around object
    cv.rectangle(img=img,
                 pt1=top_left,
                 pt2=bottom_right,
                 color=(0, 0, 255), 
                 thickness=2, 
                 lineType=cv.LINE_4)
    
    # Show box around object in base image on a popup window
    # cv.imshow('Result', img)
    # cv.waitKey()
    
    cv.imwrite('result.png', img) # Save result as file
    
else:
    print('Object was not found')