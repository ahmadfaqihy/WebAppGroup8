import streamlit as st
from PIL import Image, ImageFilter
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
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to Grayscale
    if st.button("Convert to Grayscale"):
        gray_image = image.convert("L")
        st.image(gray_image, caption="Grayscale Image", use_column_width=True)

    # Apply Blur
    if st.button("Apply Blur"):
        blurred_image = image.filter(ImageFilter.BLUR)
        st.image(blurred_image, caption="Blurred Image", use_column_width=True)

    # Advanced Processing with OpenCV
    option = st.selectbox("Choose an OpenCV Operation", ["None", "Canny Edge Detection"])
    if option == "Canny Edge Detection":
        # Convert PIL Image to OpenCV format
        opencv_image = np.array(image)
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)
        
        # Apply Canny Edge Detection
        edges = cv2.Canny(opencv_image, 100, 200)
        st.image(edges, caption="Edge Detection", use_column_width=True)

    # Download Processed Image
    st.download_button(
        label="Download Processed Image",
        data=uploaded_file.getvalue(),
        file_name="processed_image.jpg",
        mime="image/jpeg"
    )
