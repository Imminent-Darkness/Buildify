.. _api-reference:

API Reference
=============

This part of the documentation covers all the interfaces of Buildify. For parts where Buildify depends on external libraries, we document the most important right here and provide links to the canonical documentation.

.. _shopify-api:

Shopify API
-----------

The Shopify API module is responsible for all direct interactions with the Shopify store. It provides functions to create, update, and delete products and collections.

.. automodule:: shopify.shopify_api
   :members:
   :undoc-members:
   :show-inheritance:

.. _image-encoder:

Image Encoder
-------------

The Image Encoder module processes and encodes images for use in machine learning models or for display on the Shopify store.

.. automodule:: shopify.image_encoder
   :members:
   :undoc-members:
   :show-inheritance:

.. _text-encoder:

Text Encoder
------------

The Text Encoder module analyzes and encodes text data, generating numerical representations suitable for various algorithms.

.. automodule:: shopify.text_encoder
   :members:
   :undoc-members:
   :show-inheritance:

.. _fusion-strategy:

Fusion Strategy
---------------

The Fusion Strategy module clusters products based on their features and organizes them into collections on the Shopify store.

.. automodule:: shopify.fusion
   :members:
   :undoc-members:
   :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

