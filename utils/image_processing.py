def get_image_bytes(uploaded_image):
    if uploaded_image is not None:
        image_bytes = uploaded_image.getvalue()
        image_info = [{"mime_type": uploaded_image.type, "data": image_bytes}]
        return image_info
    else:
        raise FileNotFoundError("Upload a valid image file!")
