import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('uvce.jpeg', cv2.IMREAD_GRAYSCALE)

# Negative transformation
negative = 255 - image

# Log transformation
c = 255 / np.log(1 + np.max(image))
log_transformed = c * np.log(1 + image)

# Power law transformation (Gamma correction)
gamma = 0.5
power_law = np.uint8(np.power((image / 255.0), gamma) * 255)

# Contrast stretching
min_intensity = np.min(image)
max_intensity = np.max(image)
stretching = np.uint8(255 / (max_intensity - min_intensity) * (image - min_intensity))

# Displaying the images
plt.figure(figsize=(10, 10))

plt.subplot(231)
plt.imshow(image, cmap='gray')
plt.title('Original')

plt.subplot(232)
plt.imshow(negative, cmap='gray')
plt.title('Negative')

plt.subplot(233)
plt.imshow(log_transformed, cmap='gray')
plt.title('Log Transformed')

plt.subplot(234)
plt.imshow(power_law, cmap='gray')
plt.title('Power Law')

plt.subplot(235)
plt.imshow(stretching, cmap='gray')
plt.title('Contrast Stretching')

plt.tight_layout()
plt.show()
