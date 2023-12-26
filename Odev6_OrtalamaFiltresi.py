import cv2
import numpy as np

def apply_average_filter(image, kernel_size):
    # Görüntü boyutlarını al
    height, width, _ = image.shape

    # Filtrelenmiş görüntüyü saklamak için boş bir matris oluştur
    filtered_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Filtreleme işlemini uygula
    for i in range(height):
        for j in range(width):
            # Pikselin etrafındaki bölgeyi seç
            roi = image[max(0, i - kernel_size//2):min(height, i + kernel_size//2 + 1),
                        max(0, j - kernel_size//2):min(width, j + kernel_size//2 + 1)]

            # Filtrelenmiş piksel değerini hesapla
            filtered_pixel = np.mean(roi, axis=(0, 1))

            # Filtrelenmiş piksel değerini atayarak filtrelenmiş görüntüyü oluştur
            filtered_image[i, j] = filtered_pixel

    return filtered_image

# Görüntüyü yükle
image = cv2.imread('C:/Users/Emre/Desktop/image.jpg')

# Ortalama filtresi için çekirdek boyutu
kernel_size = 5

# Ortalama filtresini uygula
filtered_image = apply_average_filter(image, kernel_size)

# Giriş ve çıkış görüntülerini göster
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image (Average Filter)', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

