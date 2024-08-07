import cv2
import numpy as np

def add_text_watermark( mark, size, color, opacity, angle, space):
    # Load the image
    image = cv2.imread("C:/Users/tejas/OneDrive/Desktop/photo.jpg")
    (h, w) = image.shape[:2]

    # Create a blank image with the same dimensions for the watermark
    watermark = np.zeros((h, w, 3), dtype="uint8")

    # Set the font, scale, and thickness for the watermark text
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = size / 100
    color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) # Convert hex color to BGR
    thickness = int(size / 20)

    # Calculate the text size
    (text_w, text_h), baseline = cv2.getTextSize(mark, font, scale, thickness)
    text_h += baseline

    # Create a transparent overlay
    overlay = watermark.copy()

    # Draw the watermark text repeatedly on the overlay
    for y in range(0, h, text_h + space):
        for x in range(0, w, text_w + space):
            cv2.putText(overlay, mark, (x, y), font, scale, color, thickness, cv2.LINE_AA)

    # Rotate the overlay if an angle is specified
    if angle != 0:
        M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1)
        overlay = cv2.warpAffine(overlay, M, (w, h))

    # Blend the overlay with the original image
    cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)

    # Save the watermarked image
    

    # Display the watermarked image
    cv2.imshow('Watermarked Image', image)

    # Wait for a key press and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage

mark = 'UVCE'
size = 80
color = '#ffffff'
opacity = 0.2
angle = 30
space = 40

add_text_watermark(mark, size, color, opacity, angle, space)