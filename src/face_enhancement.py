# Face Enhancement and Beautification Filters

import cv2
import numpy as np


def enhance_face(image):
    # Convert to grayscale for facial enhancement
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Convert back to color
    enhanced_image = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

    return enhanced_image


def beautify_face(image):
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, (15, 15), 30)

    # Combine original and blurred image for a beautifying effect
    beautified_image = cv2.addWeighted(image, 0.5, blurred, 0.5, 0)

    return beautified_image


def process_image(image_path):
    image = cv2.imread(image_path)
    enhanced = enhance_face(image)
    beautified = beautify_face(enhanced)
    return beautified


if __name__ == '__main__':
    input_image_path = 'path_to_your_image.jpg'  # Replace with your image path
    output_image_path = 'output_image.jpg'
    processed_image = process_image(input_image_path)
    cv2.imwrite(output_image_path, processed_image)