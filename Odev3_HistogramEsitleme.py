import cv2
import matplotlib.pyplot as plt

# Görüntü dosyasının yolunu belirt
image_path = 'C:/Users/Emre/Desktop/image.jpg'

# Görüntüyü siyah-beyaz oku
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Histogram eşitleme işlemi
equalized_image = cv2.equalizeHist(image)

# Görüntüleri görselleştir
plt.figure(figsize=(10, 5))

# Orijinal görüntü
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Histogram eşitlenmiş görüntü
plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.show()
