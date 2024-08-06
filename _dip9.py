import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters

# Load the image
image = io.imread('flower.jpg', as_gray=True)

# Apply Sobel filter
sobel_image = filters.sobel(image)

# Apply Prewitt filter
prewitt_image = filters.prewitt(image)

# Apply Laplacian filter
laplacian_image = filters.laplace(image)

# Plot the original and filtered images
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Image')

ax[1].imshow(sobel_image, cmap='gray')
ax[1].set_title('Sobel Filter')

ax[2].imshow(prewitt_image, cmap='gray')
ax[2].set_title('Prewitt Filter')

ax[3].imshow(laplacian_image, cmap='gray')
ax[3].set_title('Laplacian Filter')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()