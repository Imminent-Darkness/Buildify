#!/usr/bin/env python3
"""
encode.py: Module for encoding text data for the Buildify project.

This module contains functions to encode text data into a format suitable for machine learning models.
The encoding process involves converting text into numerical representations, such as word embeddings
or one-hot encoded vectors, which can be used as input for various algorithms.
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np

def one_hot_encode_text(text):
    """
    One-hot encode the input text.

    :param text: A string containing the text to encode.
    :return: A one-hot encoded sparse matrix.
    """
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer(binary=True)
    
    # Fit the vectorizer on the text and transform the text
    one_hot_encoded = vectorizer.fit_transform([text])
    
    return one_hot_encoded

def tfidf_encode_text(text):
    """
    Encode the input text using TF-IDF encoding.

    :param text: A string containing the text to encode.
    :return: A TF-IDF encoded sparse matrix.
    """
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit the vectorizer on the text and transform the text
    tfidf_encoded = vectorizer.fit_transform([text])
    
    return tfidf_encoded

# Example usage
if __name__ == "__main__":
    # Example text (replace with actual text data)
    example_text = "This eco-friendly water bottle is perfect for your daily hydration needs."

    # One-hot encode the text
    one_hot_encoded_text = one_hot_encode_text(example_text)

    # TF-IDF encode the text
    tfidf_encoded_text = tfidf_encode_text(example_text)

    # Print the encoded text matrices
    print("One-hot Encoded Text:")
    print(one_hot_encoded_text.toarray())
    
    print("\nTF-IDF Encoded Text:")
    print(tfidf_encoded_text.toarray())
