import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slicing(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Initialize an array to store bit plane images
    bit_planes = []
    
    # Iterate over each bit plane (from 0 to 7)
    for i in range(8):
        # Extract the i-th bit of each pixel
        bit_plane = np.bitwise_and(gray_image, 2**i)
        
        # Append the bit plane to the list
        bit_planes.append(bit_plane)
    
    return bit_planes

# Load the image
image = cv2.imread('uvce.jpeg')

# Perform bit plane slicing
bit_planes = bit_plane_slicing(image)

# Display the original image and the bit planes
plt.figure(figsize=(10, 6))
plt.subplot(3, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

for i in range(8):
    plt.subplot(3, 3, i + 2)
    plt.imshow(bit_planes[i], cmap='gray')
    plt.title(f'Bit Plane {i}')

plt.tight_layout()
plt.show()
