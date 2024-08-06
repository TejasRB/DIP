import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread('uvce.jpeg', cv2.IMREAD_GRAYSCALE)

# Define the Laplacian kernel for sharpening
laplacian_kernel = np.array([[0, -1, 0],
                             [-1, 4, -1],
                             [0, -1, 0]])

# Apply the Laplacian kernel
laplacian_result = cv2.filter2D(image, -1, laplacian_kernel)

# Add the laplacian result back to the original image to enhance the edges
sharpened_image = cv2.add(image, laplacian_result)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.axis('off')
plt.subplot(1, 3, 2), plt.imshow(laplacian_result, cmap='gray'), plt.title('Laplacian')
plt.axis('off')
plt.subplot(1, 3, 3), plt.imshow(sharpened_image, cmap='gray'), plt.title('Sharpened')
plt.axis('off')
plt.show()
