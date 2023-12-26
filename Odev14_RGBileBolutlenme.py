import cv2
import numpy as np

def rgb_segmentation(image, lower_bound, upper_bound):
    # RGB renk modelinde bölütleme uygular
    mask = cv2.inRange(image, lower_bound, upper_bound)
    segmented_image = cv2.bitwise_and(image, image, mask=mask)
    return segmented_image

# Görüntüyü yükle
image = cv2.imread('C:/Users/Emre/Desktop/image.jpg')

# Bölütleme sınırlarını belirle
lower_blue = np.array([100, 0, 0], dtype=np.uint8)
upper_blue = np.array([255, 100, 100], dtype=np.uint8)

# RGB bölütleme uygula
segmented_image = rgb_segmentation(image, lower_blue, upper_blue)

# Görüntüleri göster
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

