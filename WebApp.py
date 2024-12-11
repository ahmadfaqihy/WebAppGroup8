import streamlit as st
from PIL import Image, ImageFilter
from io import BytesIO
import cv2
import numpy as np

# Title and Description
st.title("Image Processing Web Application")
st.write("A simple web application for basic image processing tasks.")

# File Upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert to Grayscale
    if st.button("Convert to Grayscale"):
        gray_image = image.convert("L")
        st.image(gray_image, caption="Grayscale Image", use_container_width=True)
        buffer = BytesIO()
        gray_image.save(buffer, format="JPEG")
        buffer.seek(0)
        st.download_button(
            label="Download Grayscale Image",
            data=buffer,
            file_name="grayscale_image.jpg",
            mime="image/jpeg"
    )

    # Apply Blur
    if st.button("Apply Blur"):
        blurred_image = image.filter(ImageFilter.BLUR)
        st.image(blurred_image, caption="Blurred Image", use_container_width=True)
        buffer = BytesIO()
        blurred_image.save(buffer, format="JPEG")
        buffer.seek(0)
        st.download_button(
            label="Download Blurred Image",
            data=buffer,
            file_name="blurred_image.jpg",
            mime="image/jpeg"
    )


    

