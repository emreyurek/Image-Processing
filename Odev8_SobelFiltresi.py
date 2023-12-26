import cv2
import numpy as np
from matplotlib import pyplot as plt

# Görüntüyü yükle
img = cv2.imread('C:/Users/Emre/Desktop/image.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel filtresini uygula
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # x yönlü gradient
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # y yönlü gradient

# Genel gradienti hesapla
gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)

# Giriş, x gradienti, y gradienti ve genel gradienti göster
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(2, 2, 2), plt.imshow(sobelx, cmap='gray'), plt.title('X Gradient')
plt.subplot(2, 2, 3), plt.imshow(sobely, cmap='gray'), plt.title('Y Gradient')
plt.subplot(2, 2, 4), plt.imshow(gradient_magnitude, cmap='gray'), plt.title('Genel Gradient')
plt.show()
