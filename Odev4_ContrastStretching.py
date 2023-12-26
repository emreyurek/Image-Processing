import cv2
import numpy as np

def contrast_stretching(image):
    # Görüntünün minimum ve maksimum piksel değerlerini bul
    min_val = np.min(image)
    max_val = np.max(image)

    # Kontrast germe için formülü uygula
    stretched_image = (image - min_val) * (255.0 / (max_val - min_val))

    # Piksel değerlerini sınırla (0 ile 255 arasında olmalı)
    stretched_image[stretched_image < 0] = 0
    stretched_image[stretched_image > 255] = 255

    return stretched_image.astype(np.uint8)


# Görüntüyü yükle
image = cv2.imread('C:/Users/Emre/Desktop/image.jpg', cv2.IMREAD_GRAYSCALE)

# Kontrast stretching uygula
stretched_image = contrast_stretching(image)

# Giriş ve çıkış görüntülerini göster
cv2.imshow('Original Image', image)
cv2.imshow('Contrast Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
