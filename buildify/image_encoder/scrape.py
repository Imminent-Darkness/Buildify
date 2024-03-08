#!/usr/bin/env python3
"""
scrape.py: Module for scraping images from web sources for the Buildify project.

This module contains functions to scrape images from various online sources, such as product pages,
image repositories, or search results. The scraped images can then be processed and encoded for use
in machine learning models or for display on the Shopify store.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_images_from_url(url):
    """
    Scrape all image URLs from a given web page.

    :param url: The URL of the web page to scrape.
    :return: A list of image URLs.
    """
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    # Extract the URLs of the images
    img_urls = [urljoin(url, img['src']) for img in img_tags if 'src' in img.attrs]

    return img_urls

def download_image(image_url, save_path):
    """
    Download an image from a URL and save it to the filesystem.

    :param image_url: The URL of the image to download.
    :param save_path: The path where the image will be saved.
    """
    # Send a GET request to the image URL
    response = requests.get(image_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Write the image content to a file
    with open(save_path, 'wb') as file:
        file.write(response.content)

# Example usage
if __name__ == "__main__":
    # URL of a web page to scrape (replace with an actual URL)
    page_url = 'https://example.com/product-page'

    # Scrape image URLs from the page
    image_urls = scrape_images_from_url(page_url)

    # Download the first image (replace 'path/to/save/image.jpg' with an actual path)
    if image_urls:
        download_image(image_urls[0], 'path/to/save/image.jpg')
