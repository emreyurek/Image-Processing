import cv2
import numpy as np

def gamma_correction(image, gamma):
    # Görüntüdeki her pikselin gamma düzeltmesini uygula
    corrected_image = np.power(image / 255.0, gamma) * 255.0
    
    # Piksel değerlerini sınırla (0 ile 255 arasında olmalı)
    corrected_image = np.clip(corrected_image, 0, 255)

    return corrected_image.astype(np.uint8)

# Görüntüyü yükle
image = cv2.imread('C:/Users/Emre/Desktop/image.jpg', cv2.IMREAD_GRAYSCALE)

# Gamma düzeltme için parametre
gamma_value = 1.5

# Gamma düzeltme uygula
gamma_corrected_image = gamma_correction(image, gamma_value)

# Giriş ve çıkış görüntülerini göster
cv2.imshow('Original Image', image)
cv2.imshow('Gamma Corrected Image', gamma_corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

