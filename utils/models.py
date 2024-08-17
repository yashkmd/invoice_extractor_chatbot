import google.generativeai as genai
from config.config import Config

def initialize_model(model_name=Config.MODEL_NAME):
    genai.configure(api_key=Config.API_KEY)
    model = genai.GenerativeModel(model_name)
    return model

def get_response(model, model_behavior, image, prompt):
    response = model.generate_content([model_behavior, image[0], prompt])
    return response.text
