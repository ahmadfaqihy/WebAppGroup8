import streamlit as st
from PIL import Image, ImageFilter
from io import BytesIO
import cv2
import numpy as np

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "Landing Page"

# Function to handle page navigation
def nav_bar():
    st.markdown(
        """
        <style>
        .nav-bar {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #007bff;
            padding: 10px;
            border-radius: 5px;
        }
        .nav-bar a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-size: 18px;
            font-weight: bold;
        }
        .nav-bar a:hover {
            color: #ffcccb;
        }
        .active {
            color: #ffcccb;
            text-decoration: underline;
        }
        </style>
        <div class="nav-bar">
            <a href="#" onclick="setPage('Landing Page')">Landing Page</a>
            <a href="#" onclick="setPage('Application')">Image Processing Application</a>
        </div>
        <script>
        function setPage(page) {
            fetch('/_stcore_set_state', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ key: 'current_page', value: page })
            }).then(() => location.reload());
        }
        </script>
        """,
        unsafe_allow_html=True,
    )

# Display the navigation bar
nav_bar()

# Page logic based on session state
if st.session_state.current_page == "Landing Page":
    st.title("Welcome to the Image Processing App")
    st.write(
        """
        Explore the features of this web application:
        - Upload and process images
        - Convert images to grayscale
        - Apply blur effects
        - Detect edges with advanced algorithms
        """
    )
elif st.session_state.current_page == "Application":
    st.title("Image Processing Application")
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
