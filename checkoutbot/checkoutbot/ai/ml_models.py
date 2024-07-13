import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image

def load_model(model_path):
    """
    Loads a pre-trained TensorFlow model.
    
    Args:
        model_path (str): Path to the model file.
    
    Returns:
        model: The loaded TensorFlow model.
    """
    return keras.models.load_model(model_path)

def preprocess_image(image_path):
    """
    Preprocesses an image for CAPTCHA solving.
    
    Args:
        image_path (str): Path to the CAPTCHA image.
    
    Returns:
        np.array: Preprocessed image ready for model prediction.
    """
    image = Image.open(image_path).convert('L')
    image = image.resize((100, 100))  # Resize to the expected input size of the model
    image_array = np.array(image)
    image_array = image_array / 255.0  # Normalize pixel values
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array

def solve_captcha(model, image_path):
    """
    Solves a CAPTCHA using a pre-trained model.
    
    Args:
        model (model): The pre-trained TensorFlow model.
        image_path (str): Path to the CAPTCHA image.
    
    Returns:
        str: The solved CAPTCHA text.
    """
    image_array = preprocess_image(image_path)
    prediction = model.predict(image_array)
    captcha_text = ''.join([chr(np.argmax(char)) for char in prediction])
    return captcha_text

# Example usage
# model = load_model('path_to_model.h5')
# captcha_text = solve_captcha(model, 'path_to_captcha_image.png')
# print(f'Solved CAPTCHA: {captcha_text}')
