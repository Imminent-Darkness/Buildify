#!/usr/bin/env python3
"""
update.py: Module for updating products and collections in the Shopify store for the Buildify project.

This module contains functions to update existing products and collections on Shopify using the Shopify API.
The update process involves modifying product details, prices, images, and organizing them into collections
based on the updated inventory or product range.
"""

from shopify import ShopifyAPI

def update_product(shopify_api, product_id, updated_data):
    """
    Update an existing product in the Shopify store.

    :param shopify_api: An instance of the ShopifyAPI class for making API requests.
    :param product_id: The unique identifier for the product to update.
    :param updated_data: A dictionary containing the updated product details.
    :return: The response from the Shopify API.
    """
    # Define the product update payload for the API request
    product_update_payload = {
        "product": {
            "id": product_id,
            # Include fields to update, such as title, description, etc.
            **updated_data
        }
    }

    # Update the product using the Shopify API
    response = shopify_api.update_product(product_id, product_update_payload)
    return response

def update_collection(shopify_api, collection_id, updated_data):
    """
    Update an existing collection in the Shopify store.

    :param shopify_api: An instance of the ShopifyAPI class for making API requests.
    :param collection_id: The unique identifier for the collection to update.
    :param updated_data: A dictionary containing the updated collection details.
    :return: The response from the Shopify API.
    """
    # Define the collection update payload for the API request
    collection_update_payload = {
        "custom_collection": {
            "id": collection_id,
            # Include fields to update, such as title, collects (product IDs), etc.
            **updated_data
        }
    }

    # Update the collection using the Shopify API
    response = shopify_api.update_collection(collection_id, collection_update_payload)
    return response

# Example usage
if __name__ == "__main__":
    # Initialize the Shopify API (replace with actual credentials)
    api = ShopifyAPI(api_key='your_api_key', password='your_api_password', store_url='your_store_url')

    # Example updated product data (this would be replaced with real data)
    updated_product_data = {
        'title': 'Updated Eco-friendly Water Bottle',
        'description': 'New and improved eco-friendly bottle.'
        # Add other fields to update as needed
    }

    # Update a product
    product_id_to_update = 123456789  # Replace with the actual product ID
    product_update_response = update_product(api, product_id_to_update, updated_product_data)
    print(f"Product update response: {product_update_response}")

    # Example updated collection data (this would be replaced with real data)
    updated_collection_data = {
        'title': 'Updated Eco-Friendly Collection',
        # Add other fields to update as needed
    }

    # Update a collection
    collection_id_to_update = 987654321  # Replace with the actual collection ID
    collection_update_response = update_collection(api, collection_id_to_update, updated_collection_data)
    print(f"Collection update response: {collection_update_response}")
