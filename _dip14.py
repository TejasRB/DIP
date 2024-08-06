import cv2

def restore_image(input_image_path, output_image_path, kernel_size=3):
    # Read the input image
    input_image = cv2.imread(input_image_path)
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    
    # Apply median filtering to remove noise
    restored_image = cv2.medianBlur(grayscale_image, kernel_size)
    
    # Write the restored image
    cv2.imwrite(output_image_path, restored_image)

# Example usage
input_image_path = 'noisy_image.jpeg'
output_image_path = 'restored_image.jpg'
kernel_size = 3  # Size of the median filter kernel (odd integer)

restore_image(input_image_path, output_image_path, kernel_size)
