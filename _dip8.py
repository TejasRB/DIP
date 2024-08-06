import cv2

def remove_salt_and_pepper_noise(image):
   
    return cv2.medianBlur(image, 5)  # Kernel size 5x5

# Example usage:
# Read the noisy image
noisy_img = cv2.imread('noisy_image.jpeg', 0)  # Read as grayscale

# Remove salt and pepper noise using median filter
denoised_img = remove_salt_and_pepper_noise(noisy_img)

# Display the images
cv2.imshow('Noisy Image', noisy_img)
cv2.imshow('Denoised Image', denoised_img)
cv2.waitKey(0)
cv2.destroyAllWindows()