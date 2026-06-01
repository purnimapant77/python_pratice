'''import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Input image file from user
image_path = input("Enter the path of the image: ")

# Read the image in grayscale
gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# Read the image in color (BGR)
rgb_image = cv.imread(image_path, cv.IMREAD_COLOR)

# Convert BGR to RGB
rgb_image = cv.cvtColor(rgb_image, cv.COLOR_BGR2RGB)

# Check if the images are loaded successfully
if gray_image is None or rgb_image is None:
    print("Error: Image not found or unable to read")
else:
    # Store pixel values in matrices
    gray_pixel_matrix = np.array(gray_image)
    rgb_pixel_matrix = np.array(rgb_image)

    # Display the pixel matrices
    print("Grayscale Pixel Matrix:")
    print(gray_pixel_matrix)
    print("Size of Grayscale Matrix:", gray_pixel_matrix.shape)
    print("\nRGB Pixel Matrix:")
    print(rgb_pixel_matrix)
    print("Size of RGB Matrix:", rgb_pixel_matrix.shape)

    # Display images using matplotlib
    plt.figure(figsize=(12,5))

    # Original Image
    plt.subplot(1,3,1)
    plt.imshow(cv.cvtColor(cv.imread(image_path), cv.COLOR_BGR2RGB))
    plt.title("Input Image")
    plt.axis('off')

    # Grayscale Image
    plt.subplot(1,3,2)
    plt.imshow(gray_image, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')

    # RGB Image
    plt.subplot(1,3,3)
    plt.imshow(rgb_image)
    plt.title("RGB Image")
    plt.axis('off')

    plt.show()'''
    
import cv2 as cv
import numpy as np

image_path = input("Enter the path of the image: ")

# Read the image in grayscale
gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# Read the image in RGB
rgb_image = cv.imread(image_path, cv.IMREAD_COLOR)

# Convert BGR to RGB
rgb_image = cv.cvtColor(rgb_image, cv.COLOR_BGR2RGB)

if gray_image is None or rgb_image is None:
    print("Error: Image not found or unable to read")
else:
    # Store pixel values in a 2D matrix for grayscale
    gray_pixel_matrix = np.array(gray_image)

    # Store pixel values in a 3D matrix for RGB
    rgb_pixel_matrix = np.array(rgb_image)

    # Display the pixel matrices
    print("Grayscale Pixel Matrix:")
    print(gray_pixel_matrix)
    print("Size of Grayscale Matrix:", gray_pixel_matrix.shape)
    print("\nRGB Pixel Matrix:")
    print(rgb_pixel_matrix)
    print("Size of RGB Matrix:", rgb_pixel_matrix.shape)

    # Show the images
    input_image = cv.imread(image_path) 
    cv.imshow('Input Image', input_image)
    cv.imshow('Grayscale Image', gray_image)
    cv.imshow('RGB Image', cv.cvtColor(rgb_image, cv.COLOR_RGB2BGR))
    cv.waitKey(0)
    cv.destroyAllWindows()