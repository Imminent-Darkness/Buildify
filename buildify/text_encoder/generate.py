#!/usr/bin/env python3
"""
generate.py: Module for generating text data for the Buildify project.

This module contains functions to generate text, such as product descriptions or marketing copy,
using natural language processing techniques. The generation process can involve using language models,
templates, or a combination of predefined phrases and keywords.
"""

from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_text(prompt, max_length=50):
    """
    Generate text based on a given prompt using a pre-trained GPT-2 model.

    :param prompt: A string containing the prompt to generate text from.
    :param max_length: The maximum length of the generated text sequence.
    :return: A string containing the generated text.
    """
    # Load pre-trained GPT-2 model and tokenizer
    model_name = 'gpt2'
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Encode the prompt text
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate text using the model
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)

    # Decode the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text

# Example usage
if __name__ == "__main__":
    # Example prompt (replace with an actual prompt)
    example_prompt = "Introducing our new line of eco-friendly products"

    # Generate text based on the prompt
    text = generate_text(example_prompt)

    # Print the generated text
    print(f"Generated Text: {text}")
