import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Input image file from user
image_path = input("Enter the path of the image: ")

# Read the image in grayscale
gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# Read the image in RGB (BGR in OpenCV)
rgb_image = cv.imread(image_path, cv.IMREAD_COLOR)

# Check if images are loaded successfully
if gray_image is None or rgb_image is None:
    print("Error: Image not found or unable to read")
else:
    # -----------------------------
    # Image display (simulating cv.imshow)
    # -----------------------------
    # Input image
    plt.figure()
    plt.imshow(cv.cvtColor(cv.imread(image_path), cv.COLOR_BGR2RGB))
    plt.title("Input Image")
    plt.axis('off')
    plt.show()

    # Grayscale image
    plt.figure()
    plt.imshow(gray_image, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')
    plt.show()

    # RGB image
    plt.figure()
    plt.imshow(cv.cvtColor(rgb_image, cv.COLOR_BGR2RGB))
    plt.title("RGB Image")
    plt.axis('off')
    plt.show()

    # -----------------------------
    # Grayscale histogram
    # -----------------------------
    plt.figure()
    plt.title("Grayscale Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.hist(gray_image.ravel(), bins=256, range=[0, 256], color='black', alpha=0.75)
    plt.show()

    # -----------------------------
    # RGB histograms
    # -----------------------------
    colors = ('b', 'g', 'r')  # BGR channel order
    plt.figure()
    plt.title("RGB Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    for i, color in enumerate(colors):
        hist = cv.calcHist([rgb_image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=f'{color.upper()} Channel')
    plt.legend()
    plt.show()