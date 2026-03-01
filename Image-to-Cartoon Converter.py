import cv2
import numpy as np
import matplotlib.pyplot as plt

def cartoonize_image(img_path):
    # Read the image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # STEP 1 & 2: Gray and Blur
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)

    # STEP 3: Create Edges (Outlines)
    # 9, 9 are the block size and constant subtracted from mean
    edges = cv2.adaptiveThreshold(gray_blur, 255, 
                                  cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 9, 9)

    # STEP 4: Smooth Colors (Surface)
    # d=9: Neighborhood diameter
    # sigmaColor=300, sigmaSpace=300: High values for a strong cartoon effect
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # STEP 5: Combine Edges + Color
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return img, edges, cartoon

# Visualize the Output
original, outlines, final = cartoonize_image("your_photo.jpg")

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1); plt.imshow(original); plt.title("Original")
plt.subplot(1, 3, 2); plt.imshow(outlines, cmap='gray'); plt.title("Edge Mask")
plt.subplot(1, 3, 3); plt.imshow(final); plt.title("Final Cartoon")
plt.show()
