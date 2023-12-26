import cv2
import numpy as np
from matplotlib import pyplot as plt

# Görüntüyü yükle
img = cv2.imread('C:/Users/Emre/Desktop/image.jpg', cv2.IMREAD_GRAYSCALE)

# Gaussian filtresini uygula (blurring)
ksize = (5, 5)  # Filtre boyutu
sigma = 1.5     # Standart sapma
blurred_img = cv2.GaussianBlur(img, ksize, sigma)

# Laplace filtresini uygula
laplacian = cv2.Laplacian(blurred_img, cv2.CV_64F)

# Giriş, blurlanmış ve Laplace filtreli görüntüyü göster
plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(132), plt.imshow(blurred_img, cmap='gray'), plt.title('Blurlanmış Görüntü')
plt.subplot(133), plt.imshow(laplacian, cmap='gray'), plt.title('Laplace Filtreli')
plt.show()
