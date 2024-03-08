#!/usr/bin/env python3
"""
cluster.py: Module for clustering products into collections for the Buildify project.

This module contains functions to cluster products based on their features using machine learning algorithms.
The clustering process groups similar products together, which can then be used to create collections
on the Shopify store.
"""

from sklearn.cluster import KMeans
import numpy as np

def perform_kmeans_clustering(features, num_clusters):
    """
    Perform K-means clustering on product features to group them into clusters.

    :param features: A 2D numpy array where each row represents a product's features.
    :param num_clusters: The number of clusters to form.
    :return: A tuple containing the cluster labels and the KMeans model.
    """
    # Initialize the KMeans model with the desired number of clusters
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)

    # Fit the model to the data
    kmeans.fit(features)

    # Get the cluster labels for each product
    labels = kmeans.labels_

    return labels, kmeans

def create_product_clusters(products, labels):
    """
    Create clusters of products based on the labels provided by the clustering algorithm.

    :param products: A list of product dictionaries with product details.
    :param labels: A list of cluster labels corresponding to each product.
    :return: A dictionary of clusters with products grouped under their respective cluster label.
    """
    clusters = {}
    for product, label in zip(products, labels):
        # If the cluster label does not exist in the dictionary, create a new list
        if label not in clusters:
            clusters[label] = []

        # Append the product to the appropriate cluster
        clusters[label].append(product)

    return clusters

# Example usage
if __name__ == "__main__":
    # Example product features (this would be replaced with real data)
    example_features = np.array([
        [1.0, 0.2, 0.4],
        [0.9, 0.1, 0.5],
        [0.0, 1.0, 0.0],
        [0.1, 0.9, 0.2]
    ])

    # Example products (this would be replaced with real data)
    example_products = [
        {'name': 'Product 1', 'description': 'An eco-friendly product'},
        {'name': 'Product 2', 'description': 'Another eco-friendly product'},
        {'name': 'Product 3', 'description': 'A different kind of product'},
        {'name': 'Product 4', 'description': 'Yet another different product'}
    ]

    # Perform clustering
    num_clusters = 2  # This is an arbitrary choice for demonstration purposes
    labels, model = perform_kmeans_clustering(example_features, num_clusters)

    # Create product clusters
    product_clusters = create_product_clusters(example_products, labels)

    # Print the clusters
    for label, products in product_clusters.items():
        print(f"Cluster {label}:")
        for product in products:
            print(f"- {product['name']}: {product['description']}")
