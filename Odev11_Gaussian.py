import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernel(size, sigma=1.0):
    # Gaussian kernel oluştur
    kernel = np.fromfunction(
        lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x-(size-1)/2)**2 + (y-(size-1)/2)**2)/(2*sigma**2)),
        (size, size)
    )
    return kernel / np.sum(kernel)

def my_gaussian_filter(image, kernel):
    # Gaussian filtresi uygula
    height, width = image.shape[:2]
    k_size = len(kernel)
    pad = k_size // 2
    result = np.zeros((height, width), dtype=np.float32)

    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            window = image[i - pad:i + pad + 1, j - pad:j + pad + 1]
            result[i, j] = np.sum(window * kernel)

    return result.astype(np.uint8)

# Görüntüyü yükle
image = cv2.imread('C:/Users/Emre/Desktop/image.jpg', cv2.IMREAD_GRAYSCALE)

# Gaussian kernel oluştur
kernel_size = 5
sigma = 1.0
gaussian_kernel_matrix = gaussian_kernel(kernel_size, sigma)

# Gaussian filtresini uygula
filtered_image = my_gaussian_filter(image, gaussian_kernel_matrix)

# Görüntüleri göster
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Filtered Image')
plt.imshow(filtered_image, cmap='gray')

plt.show()
