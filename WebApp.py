import streamlit as st
from PIL import Image, ImageFilter
from io import BytesIO
import cv2
import numpy as np
import streamlit as st
from PIL import Image, ImageFilter
from io import BytesIO

# Sidebar navigation
menu = st.sidebar.selectbox("Select Page", ["Home", "Apply Filter"])

# Landing Page
if menu == "Home":
    st.markdown(
        """
        <style>
        .Home {
            text-align: center;
            padding: 50px;
            background-color: #f8f9fa;
            border-radius: 5px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="Home">
            <h1>Welcome to the Image Processing App</h1>
            <p>Explore the capabilities of this web application:</p>
            <ul style="text-align: left;">
                <li>Upload and process your images</li>
                <li>Convert to grayscale, blur, and apply edge detection</li>
                <li>Download the processed images</li>
            </ul>
            <p>Use the sidebar to navigate to the application!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Apply Filter
elif menu == "Apply Filter":
    st.title("Apply Filter")
    st.write("Upload an image and perform basic processing tasks.")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert to Grayscale
        if st.button("Convert to Grayscale"):
            gray_image = image.convert("L")
            st.image(gray_image, caption="Grayscale Image", use_column_width=True)

            # Download Grayscale Image
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
            st.image(blurred_image, caption="Blurred Image", use_column_width=True)

            # Download Blurred Image
            buffer = BytesIO()
            blurred_image.save(buffer, format="JPEG")
            buffer.seek(0)
            st.download_button(
                label="Download Blurred Image",
                data=buffer,
                file_name="blurred_image.jpg",
                mime="image/jpeg"
            )
