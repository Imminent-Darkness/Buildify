#!/usr/bin/env python3
"""
encode.py: Module for encoding images for the Buildify project.

This module contains functions to encode images into a suitable format for machine learning models.
The encoding process typically involves resizing images, normalizing pixel values, and possibly
extracting features using pre-trained neural networks.
"""

from PIL import Image
import numpy as np
import torchvision.transforms as transforms
from torchvision.models import resnet50
import torch

def load_image(image_path):
    """
    Load an image from the filesystem.

    :param image_path: The path to the image file.
    :return: An Image object.
    """
    return Image.open(image_path)

def preprocess_image(image):
    """
    Preprocess the image for encoding.

    :param image: An Image object.
    :return: A preprocessed image tensor.
    """
    # Define the image transformations
    preprocess = transforms.Compose([
        transforms.Resize(256),             # Resize the image to 256x256 pixels
        transforms.CenterCrop(224),         # Crop the center 224x224 pixels
        transforms.ToTensor(),              # Convert the image to a PyTorch tensor
        transforms.Normalize(               # Normalize the image
            mean=[0.485, 0.456, 0.406],    # These are the ImageNet mean values
            std=[0.229, 0.224, 0.225]      # These are the ImageNet std deviation values
        )
    ])

    # Apply the transformations to the image
    image_tensor = preprocess(image)
    return image_tensor

def encode_image(image_tensor):
    """
    Encode the image using a pre-trained ResNet-50 model.

    :param image_tensor: A preprocessed image tensor.
    :return: An encoded feature vector.
    """
    # Load a pre-trained ResNet-50 model
    model = resnet50(pretrained=True)
    model.eval()  # Set the model to evaluation mode

    # Remove the last fully connected layer (classification layer)
    model = torch.nn.Sequential(*(list(model.children())[:-1]))

    # Encode the image
    with torch.no_grad():  # No need to compute gradients
        encoded_image = model(image_tensor.unsqueeze(0))  # Add a batch dimension

    # Flatten the features to a vector
    encoded_vector = encoded_image.flatten().numpy()
    return encoded_vector

# Example usage
if __name__ == "__main__":
    # Load an image (replace 'path/to/image.jpg' with the actual image path)
    image = load_image('path/to/image.jpg')

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Encode the image
    encoded_vector = encode_image(preprocessed_image)

    # Print the encoded feature vector
    print(f"Encoded image vector: {encoded_vector}")
