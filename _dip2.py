import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load two images
img1 = cv2.imread('uvce.jpeg')
img2 = cv2.imread('flower.jpg')

# Perform arithmetic operations
add = cv2.add(img1, img2)
subtract = cv2.subtract(img1, img2)
multiply = cv2.multiply(img1, img2)
divide = cv2.divide(img1, img2)

# Perform logical operations
bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)
bitwise_not_img1 = cv2.bitwise_not(img1)
bitwise_not_img2 = cv2.bitwise_not(img2)

# Display results
titles = ['Addition', 'Subtraction', 'Multiplication', 'Division',
          'Bitwise AND', 'Bitwise OR', 'Bitwise XOR', 'Bitwise NOT (Image 1)', 'Bitwise NOT (Image 2)']
images = [add, subtract, multiply, divide,
          bitwise_and, bitwise_or, bitwise_xor, bitwise_not_img1, bitwise_not_img2]

for i in range(len(images)):
    plt.subplot(3, 3, i+1), plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
