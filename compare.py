from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse
import sys
## [Load three images with different environment settings]


src_base = cv.imread(sys.argv[1])
src_test1 = cv.imread(sys.argv[2])

if src_base is None or src_test1 is None :
    print('Could not open or find the images!')
    exit(0)
## [Load three images with different environment settings]

## [Convert to HSV]
hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
hsv_test1 = cv.cvtColor(src_test1, cv.COLOR_BGR2HSV)

## [Convert to HSV]

## [Convert to HSV half]

## [Convert to HSV half]

## [Using 50 bins for hue and 60 for saturation]
h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]

# hue varies from 0 to 179, saturation from 0 to 255
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges # concat lists

# Use the 0-th and 1-st channels
channels = [0, 1]
## [Using 50 bins for hue and 60 for saturation]

## [Calculate the histograms for the HSV images]
hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

hist_test1 = cv.calcHist([hsv_test1], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test1, hist_test1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)


## [Calculate the histograms for the HSV images]

## [Apply the histogram comparison methods]

base_base = cv.compareHist(hist_base, hist_base, 3)
base_test1 = cv.compareHist(hist_base, hist_test1, 3)

print(1-base_test1)
f=open("back.txt","w")
f.write(str(1-base_test1))
## [Apply the histogram comparison methods]