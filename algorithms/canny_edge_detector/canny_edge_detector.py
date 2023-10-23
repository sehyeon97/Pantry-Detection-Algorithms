# Canny Edge Detector uses a number of diverse image datasets
# in order to identify the edges in different types of
# images under various conditions

# 4 major steps
# 1. Reduce Noise using Gaussian Smoothing
# -- allows us to ignore much of the detail and instead focus on the actual structure of object
# 2. Compute Gradient magnitude and orientation
# -- Gradient magnitude is susceptible to noise, therefore apply the bottom 2 steps
# 3. Apply Non-Max Suppression (edge thinning process)
# -- still no idea what step 3 does
# 4. Apply Hysteresis thresholding (upper_threshold, lower_threshold) for the Canny() function
# -- Mark as edge if gradient value is a strong edge i.e. G > upper_threshold
# -- Discard gradient pixel if G < lower_threshold
# -- Open Hysteresis_thresholding.png within this folder for more info

# Because Canny Edge is well known in edge detection,
# OpenCV has already implemented it for other developers
# in the cv2.Canny function

# One potential downfall is lighting
# If there is light shining down on some object
# the shape the light makes on the object will be seen as an edge of the object

import cv2
import argparse

# load the image, convert it to grayscale and blur it slightly
image = cv2.imread(
    "C:/Users/sehye/OneDrive/Desktop/pantry/algorithms/canny_edge_detector/test.png"
)
print(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# show the original and blurred images
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

# compute a "wide", "mid-range", and "tight" threshold for the edges
# using the Canny edge detector
wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

# show the output Canny edge maps
cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.waitKey(0)
