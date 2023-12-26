import numpy as np
import cv2
import matplotlib.pyplot as plt

# Görüntü dosyasının yolunu belirt
image_path = 'C:/Users/Emre/Desktop/image.jpg'  

def bit_plane_slicing(image_path):
    # Görüntüyü siyah-beyaz oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Görüntü yüklenemedi. Dosya yolunu kontrol edin.")
        return

    # Her bir bit düzlemini saklamak için boş bir dizi oluştur
    bit_planes = []
    
    # Görüntünün boyutlarını al
    rows, cols = image.shape
    
    # Her bir bit düzlemini oluştur ve diziye ekle
    for i in range(8):
        # Her bir bit düzlemi için boş bir NumPy dizisi oluştur
        # İlgili bit değerini alarak ve 255 ile çarparak bit düzlemini oluştur
        bit_plane = (image & (1 << i)) * 255
    
        # Oluşturulan bit düzlemini bit_planes dizisine ekle
        bit_planes.append(bit_plane)

    # Bit düzlemlerini görselleştir
    plt.figure(figsize=(15, 10))

    for i in range(8):
        # Her bir bit düzlemini ayrı bir alt grafikte göster
        plt.subplot(3, 3, i + 1)
        plt.imshow(bit_planes[i], cmap='gray')
        plt.title('Bit Plane ' + str(i))
        plt.xticks([]), plt.yticks([])

    # Orjinal görüntüyü göster
    plt.subplot(3, 3, 9)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.xticks([]), plt.yticks([])

    # Görseli göster
    plt.show()

# Fonksiyonu çağırarak işlemi başlat
bit_plane_slicing(image_path)
