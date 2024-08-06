import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_frequency_filter(img, filter_type, cutoff):
    # FFT to convert image to frequency domain
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)

    # Create mask
    rows, cols = img.shape
    crow, ccol = rows // 2 , cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow-cutoff:crow+cutoff, ccol-cutoff:ccol+cutoff] = 1

    if filter_type == 'highpass':
        mask = 1 - mask

    # Apply mask and inverse FFT
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    return img_back

# Load image in grayscale
image = cv2.imread('uvce.jpeg', 0)

# Apply Filters
low_pass_img = apply_frequency_filter(image, 'lowpass', 30)
high_pass_img = apply_frequency_filter(image, 'highpass', 30)

# Display images
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.axis('off')
plt.subplot(1, 3, 2), plt.imshow(low_pass_img, cmap='gray'), plt.title('Low Pass')
plt.axis('off')
plt.subplot(1, 3, 3), plt.imshow(high_pass_img, cmap='gray'), plt.title('High Pass')
plt.axis('off')
plt.show()
