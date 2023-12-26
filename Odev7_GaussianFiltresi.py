import cv2
import numpy as np
from matplotlib import pyplot as plt

# Görüntüyü yükle
img = cv2.imread('C:/Users/Emre/Desktop/image.jpg')

# Gaussian filtresini uygula
ksize = (5, 5)  # Filtre boyutu
sigma = 1.5     # Standart sapma
filtered_img = cv2.GaussianBlur(img, ksize, sigma)

# Giriş ve çıkış görüntülerini göster
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)), plt.title('Gaussian Filtreli Görüntü')
plt.show()