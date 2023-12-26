import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle (örneğin, siyah zemin üzerinde beyaz nesneler içeren bir görüntü)
image = cv2.imread('C:/Users/Emre/Desktop/image.jpg', cv2.IMREAD_GRAYSCALE)

# Açma işlemi
kernel_size_opening = 5
kernel_opening = np.ones((kernel_size_opening, kernel_size_opening), np.uint8)
opening_result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel_opening)

# Kapama işlemi
kernel_size_closing = 5
kernel_closing = np.ones((kernel_size_closing, kernel_size_closing), np.uint8)
closing_result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_closing)

# Görüntüleri göster
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(opening_result, cmap='gray')
plt.title('Opening Result')

plt.subplot(1, 3, 3)
plt.imshow(closing_result, cmap='gray')
plt.title('Closing Result')

plt.show()
