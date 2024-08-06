import cv2
import matplotlib.pyplot as plt

def edge_detection(image_path, low_threshold, high_threshold):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if image is loaded successfully
    if image is None:
        print("Error: Image not loaded correctly")
        return

    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)

    # Perform Canny edge detection
    edges = cv2.Canny(blurred_image, low_threshold, high_threshold)

    # Display the original and edge-detected images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Edge-detected Image')
    plt.imshow(edges, cmap='gray')
    plt.axis('off')

    plt.show()

# Parameters
image_path = 'flower.jpg'  # Replace with your image path
low_threshold = 50
high_threshold = 150

# Perform edge detection
edge_detection(image_path, low_threshold, high_threshold)
