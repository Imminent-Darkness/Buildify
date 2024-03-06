import pytest 
from shopify.image_encoder import scrape, process, encode

def test_scrape_images():
    # GIVEN a URL of a Shopify store
    # WHEN the scrape function is called
    # THEN it should return a list of image URLs
    assert isinstance(scrape('shopify_store_url'), list)

def test_process_images():
    # GIVEN a list of image URLs
    # WHEN the process function is called
    # THEN it should return a list of processed images
    assert isinstance(process(['image_url1', 'image_url2']), list)

def test_encode_images():
    # GIVEN a list of processed images
    # WHEN the encode function is called
    # THEN it should return a list of image encodings
    assert isinstance(encode(['processed_image_1', 'processed_image_2']), list)



