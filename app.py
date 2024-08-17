import streamlit as st
from PIL import Image
from utils.models import initialize_model, get_response
from utils.image_processing import get_image_bytes
from config.config import Config

# Initialize the model
model = initialize_model(Config.MODEL_NAME)

# Set up Streamlit page
st.set_page_config("Invoice Extractor")
st.header("Invoice Extractor")

# Chat interface
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create columns for side-by-side layout
col1, col2 = st.columns(2)

# Image uploader in the first column
with col1:
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

# Set the model behavior
model_behavior = """
You are an expert who understands invoice overall structures and has deep knowledge on it.
We will upload the invoice image and you have to answer the question based on information 
present in the invoice image.
"""

# Display the uploaded image in the second column
if uploaded_image is not None:
    with col2:
        image = Image.open(uploaded_image)
        st.image(image, caption="Your image", use_column_width=True)

# Chat input
if prompt := st.chat_input("Enter your prompt"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if uploaded_image is not None:
        image_info = get_image_bytes(uploaded_image)
        
        # Get response from model
        response = get_response(model, model_behavior, image_info, prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
    else:
        st.session_state.messages.append({"role": "assistant", "content": "Please upload an image to proceed."})
        with st.chat_message("assistant"):
            st.markdown("Please upload an image to proceed.")
