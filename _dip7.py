import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread('uvce.jpeg', cv2.IMREAD_GRAYSCALE)

# Define low pass filter (smoothing) - averaging kernel
low_pass_kernel = np.ones((5, 5), np.float32) / 25

# Apply low pass filter
smoothed_image = cv2.filter2D(image, -1, low_pass_kernel)

# Define high pass filter (sharpening) - Laplacian kernel
high_pass_kernel = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])

# Apply high pass filter
sharpened_image = cv2.filter2D(image, -1, high_pass_kernel)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.axis('off')
plt.subplot(1, 3, 2), plt.imshow(smoothed_image, cmap='gray'), plt.title('Low Pass (Smoothed)')
plt.axis('off')
plt.subplot(1, 3, 3), plt.imshow(sharpened_image, cmap='gray'), plt.title('High Pass (Sharpened)')
plt.axis('off')
plt.show()
