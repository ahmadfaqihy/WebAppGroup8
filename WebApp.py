import streamlit as st
from PIL import Image, ImageFilter
from io import BytesIO
import cv2
import numpy as np

  <nav class="navbar navbar-expand-lg navbar-dark shadow" style="background-color:rgb(39, 66, 66)"
>
    <div class="container-fluid">
      
      <a class="navbar-brand" href="" style="padding-left:4rem ;"><i class="fas fa-circle-notch"></i></a>
      <a class="navbar-brand" href="#Ahmad" style="padding-left:1rem ;">Ahmad Faqih Yassin</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link" href="#About Me">About Me</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#Biodata">Biodata</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#Gallery">Highlight</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="Gallery.html"><i class="far fa-image"></i></a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#FindMe" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
           Find Me
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="#Email">Email</a></li>
              <li><a class="dropdown-item" href="#YouTube">YouTube</a></li>
              <li><a class="dropdown-item" href="#Instagram">Instagram</a></li>
              <li><a class="dropdown-item" href="#Twitter">Twitter</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>

# Landing Page
if menu == "Landing Page":
    st.markdown(
        """
        <style>
        .landing-page {
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
        <div class="landing-page">
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

# Image Processing Application
elif menu == "Image Processing Application":
    st.title("Image Processing Application")
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


