from shopify.text_encoder import analyze, generate, encode

def test_analyze_text():
    # GIVEN a product description
    # WHEN the analyze function is called
    # THEN it should return a list of keywords
    assert isinstance(analyze('product_description'), list)

def test_generate_text():
    # GIVEN a list of keywords
    # WHEN the generate function is called
    # THEN it should return a generated product description
    assert isinstance(generate(['keyword1', 'keyword2']), str)

def test_encode_text():
    # GIVEN a product description
    # WHEN the encode function is called
    # THEN it should return an encoded product description
    assert isinstance(encode('product_description'), list)

