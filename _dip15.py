import numpy as np
import cv2
import matplotlib.pyplot as plt

def block_truncation_coding(image, block_size):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape

    # Initialize the compressed image
    compressed_image = np.zeros_like(gray_image)

    # Process each block
    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block = gray_image[i:i+block_size, j:j+block_size]
            
            # Calculate mean value of the block
            mean = np.mean(block)
            
            # Create the bitmask and two representative values
            bitmask = block >= mean
            high_value = block[bitmask].mean() if np.any(bitmask) else mean
            low_value = block[~bitmask].mean() if np.any(~bitmask) else mean
            
            # Reconstruct the block using the bitmask and representative values
            compressed_block = np.where(bitmask, high_value, low_value)
            compressed_image[i:i+block_size, j:j+block_size] = compressed_block

    return compressed_image

# Load the image
image_path = 'flower.jpg'
image = cv2.imread(image_path)

# Set block size
block_size = 100

# Perform Block Truncation Coding
compressed_image = block_truncation_coding(image, block_size)

# Display the original and compressed images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Compressed Image')
plt.imshow(compressed_image, cmap='gray')
plt.axis('off')

plt.show()
