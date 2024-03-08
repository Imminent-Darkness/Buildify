#!/usr/bin/env python3
"""
analyze.py: Module for analyzing text data for the Buildify project.

This module contains functions to analyze text data, such as product descriptions or reviews.
The analysis can include natural language processing tasks like tokenization, part-of-speech tagging,
named entity recognition, sentiment analysis, and keyword extraction.
"""

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Ensure that the necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
nltk.download('stopwords')

def tokenize_text(text):
    """
    Tokenize the input text into words.

    :param text: A string containing the text to tokenize.
    :return: A list of words.
    """
    return word_tokenize(text)

def remove_stopwords(words):
    """
    Remove common stopwords from a list of words.

    :param words: A list of words.
    :return: A list of words without stopwords.
    """
    stop_words = set(stopwords.words('english'))
    return [word for word in words if word not in stop_words]

def analyze_sentiment(text):
    """
    Analyze the sentiment of the input text.

    :param text: A string containing the text to analyze.
    :return: A dictionary with sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

def extract_keywords(words, num_keywords=5):
    """
    Extract the most common keywords from a list of words.

    :param words: A list of words.
    :param num_keywords: The number of keywords to extract.
    :return: A list of keywords.
    """
    counter = Counter(words)
    most_common = counter.most_common(num_keywords)
    return [keyword for keyword, _ in most_common]

# Example usage
if __name__ == "__main__":
    # Example text (replace with actual text data)
    example_text = "This eco-friendly water bottle is perfect for your daily hydration needs."

    # Tokenize the text
    tokens = tokenize_text(example_text)

    # Remove stopwords
    filtered_tokens = remove_stopwords(tokens)

    # Analyze sentiment
    sentiment_scores = analyze_sentiment(example_text)

    # Extract keywords
    keywords = extract_keywords(filtered_tokens)

    # Print the results
    print(f"Tokens: {tokens}")
    print(f"Filtered Tokens: {filtered_tokens}")
    print(f"Sentiment Scores: {sentiment_scores}")
    print(f"Keywords: {keywords}")
