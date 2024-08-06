import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# Load the image
image = cv2.imread('uvce.jpeg')
 
# Display the original image
plt.subplot(3, 3, 1)  # Changed to 3x3 grid
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
 
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(3, 3, 2)  # Changed to 3x3 grid
plt.title('Grayscale Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
 
# Split the image into red, green, and blue channels
b, g, r = cv2.split(image)

# Display Red Channel
plt.subplot(3, 3, 4)  # Changed to 3x3 grid, corrected position
plt.title('Red Channel')
plt.imshow(r, cmap='gray')
plt.axis('off')
 
# Display Green Channel
plt.subplot(3, 3, 5)  # Changed to 3x3 grid, corrected position
plt.title('Green Channel')
plt.imshow(g, cmap='gray')
plt.axis('off')
 
# Display Blue Channel
plt.subplot(3, 3, 6)  # Changed to 3x3 grid, corrected position
plt.title('Blue Channel')
plt.imshow(b, cmap='gray')
plt.axis('off')
 
# Perform 1D convolution
kernel_1d = np.array([1, 0, -1])
conv_1d_image = cv2.filter2D(gray_image, -1, kernel_1d)
plt.subplot(3, 3, 7)  # Changed to 3x3 grid, corrected position
plt.title('1D Convolution')
plt.imshow(conv_1d_image, cmap='gray')
plt.axis('off')
 
# Perform 2D convolution
kernel_2d = np.array([[1, 1, 1],
                      [1, -8, 1],
                      [1, 1, 1]])
conv_2d_image = cv2.filter2D(gray_image, -1, kernel_2d)
plt.subplot(3, 3, 8)  # Changed to 3x3 grid, corrected position
plt.title('2D Convolution')
plt.imshow(conv_2d_image, cmap='gray')
plt.axis('off')
 
plt.tight_layout()
plt.show()
