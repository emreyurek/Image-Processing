import cv2
import numpy as np

def contraharmonic_mean_filter(image, kernel_size, Q):
    result = np.copy(image)
    height, width = image.shape

    pad = kernel_size // 2

    for i in range(pad, height - pad):
        for j in range(pad, width - pad):
            window = image[i - pad:i + pad + 1, j - pad:j + pad + 1]
            numerator = np.sum(window**(Q + 1))
            denominator = np.sum(window**Q)

            result[i, j] = numerator / denominator if denominator != 0 else 0

    return result.astype(np.uint8)

# Görüntüyü yükle
image = cv2.imread('C:/Users/Emre/Desktop/image.jpg', cv2.IMREAD_GRAYSCALE)

# Contraharmonic Mean filtresini uygula (örneğin, kernel boyutu 3x3, Q=1.5)
filtered_image = contraharmonic_mean_filter(image, kernel_size=3, Q=1.5)

# Görüntüleri göster
cv2.imshow('Original Image', image)
cv2.imshow('Contraharmonic Mean Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
