import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread('cman.png', cv2.IMREAD_GRAYSCALE)

# Apply Otsu's thresholding
ret, otsu_segmentation = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2), plt.imshow(otsu_segmentation, cmap='gray'), plt.title('Otsu Segmentation')
plt.axis('off')
plt.show()
