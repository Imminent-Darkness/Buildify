#!/usr/bin/env python3
"""
process.py: Module for processing images for the Buildify project.

This module contains functions to process images before they are encoded. Processing can include
resizing, cropping, color adjustments, and other image manipulations to ensure consistency and
optimal input for machine learning models.
"""

from PIL import Image, ImageOps

def resize_image(image, size=(224, 224)):
    """
    Resize an image to the specified size.

    :param image: An Image object.
    :param size: A tuple indicating the new size (width, height).
    :return: A resized Image object.
    """
    return image.resize(size, Image.ANTIALIAS)

def convert_to_grayscale(image):
    """
    Convert an image to grayscale.

    :param image: An Image object.
    :return: A grayscale Image object.
    """
    return ImageOps.grayscale(image)

def crop_center(image):
    """
    Crop the center of the image.

    :param image: An Image object.
    :return: A cropped Image object.
    """
    width, height = image.size
    new_width, new_height = min(width, height), min(width, height)
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    return image.crop((left, top, right, bottom))

def enhance_contrast(image, factor=1.5):
    """
    Enhance the contrast of an image.

    :param image: An Image object.
    :param factor: Contrast enhancement factor.
    :return: An Image object with enhanced contrast.
    """
    from PIL import ImageEnhance
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

# Example usage
if __name__ == "__main__":
    # Load an image (replace 'path/to/image.jpg' with the actual image path)
    image_path = 'path/to/image.jpg'
    image = Image.open(image_path)

    # Process the image
    resized_image = resize_image(image)
    grayscale_image = convert_to_grayscale(resized_image)
    cropped_image = crop_center(grayscale_image)
    final_image = enhance_contrast(cropped_image)

    # Save the processed image (replace 'path/to/processed_image.jpg' with the actual save path)
    save_path = 'path/to/processed_image.jpg'
    final_image.save(save_path)
