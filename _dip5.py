import cv2
from matplotlib import pyplot as plt

# Load the image in color
image = cv2.imread('flower.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB

# Convert the image from RGB to YCrCb
ycrcb_image = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)

# Split the channels
Y, Cr, Cb = cv2.split(ycrcb_image)

# Apply histogram equalization to the Y channel
equalized_Y = cv2.equalizeHist(Y)

# Merge the channels
equalized_image = cv2.merge((equalized_Y, Cr, Cb))

# Convert back to RGB
equalized_image = cv2.cvtColor(equalized_image, cv2.COLOR_YCrCb2RGB)

# Display the original and enhanced images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image)
plt.title('Enhanced Image')
plt.axis('off')

plt.show()
