import cv2
import numpy as np

# Read the image
image = cv2.imread('uvce.jpeg', 0)  # Read the image in grayscale

# Define the structuring element
kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(image, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(image, kernel, iterations=1)

# Opening
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Closing
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
