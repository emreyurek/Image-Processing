import cv2
import numpy as np

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)

    # Salt gürültüsü ekle
    salt_pixels = np.random.rand(*image.shape[:2]) < salt_prob
    noisy_image[salt_pixels] = 255

    # Pepper gürültüsü ekle
    pepper_pixels = np.random.rand(*image.shape[:2]) < pepper_prob
    noisy_image[pepper_pixels] = 0

    return noisy_image

# Görüntüyü yükle
image = cv2.imread('C:/Users/Emre/Desktop/image.jpg', cv2.IMREAD_GRAYSCALE)

# Salt and pepper gürültüsü ekle
noisy_image = add_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02)

# Görüntüleri göster
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
