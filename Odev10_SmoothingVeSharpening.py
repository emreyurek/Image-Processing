import cv2
import numpy as np

def my_smoothing(image, kernel_size):
    # ortalama filtresi uygula
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)
    smoothed_image = cv2.filter2D(image, -1, kernel)
    return smoothed_image

def my_sharpening(image):
    # Laplacian filtresi uygula
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    
    # Görüntüyü keskinleştir
    sharpened_image = image - laplacian
    
    # Negatif değerleri sıfıra eşitle
    sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)
    
    return sharpened_image

# Görüntüyü yükle
image = cv2.imread('C:/Users/Emre/Desktop/image.jpg')

# Smoothing uygula
smoothed_image = my_smoothing(image, 5)

# Sharpening uygula
sharpened_image = my_sharpening(image)

# Görüntüleri göster
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
