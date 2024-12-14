import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
from io import BytesIO
import cv2
import numpy as np

# Sidebar navigation
menu = st.sidebar.selectbox("Select Page", ["Home", "Meet the Members", "Apply Filter"])

# Landing Page
if menu == "Home":
    st.markdown(
        """
        <style>
        .Home {
            text-align: center;
            padding: 50px;
            background-color: #edeefc;
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
            <h1>Welcome to Group 8 Website Image Filtering Application!</h1>
            <h5>Explore various capability to alter your image using the application of Image Processing with Linear Algebra Principle:</h5>
            <ul style="text-align: left;">
                <li>Upload and process your images</li>
                <li>Convert to grayscale, blur, sepia tone, contour, sharpness adjustment, and many more!</li>
                <li>Download the processed images</li>
            </ul>
            <p>Use the sidebar to navigate to the application.</p>
            <p>Group 8 - N IE 01</p>
            <p>Industrial Engineering - Faculty of Engineering</p>
            <img src="https://raw.githubusercontent.com/ahmadfaqihy/WebAppGroup8/refs/heads/master/logo%20pu%20removed.png" alt="Logo" style="width: 200px; display: block; margin-left: auto; margin-right: auto;">
        </div>
        """,
        unsafe_allow_html=True,
    )

elif menu == "Apply Filter":
    st.title("Apply Filter")
    st.write("Upload an image and perform various processing tasks.")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Convert to Grayscale"):
            gray_image = image.convert("L")
            st.image(gray_image, caption="Grayscale Image", use_container_width=True)
            
        if st.button("Apply Blur"):
            blurred_image = image.filter(ImageFilter.BLUR)
            st.image(blurred_image, caption="Blurred Image", use_container_width=True)

        sharpness_factor = st.slider("Adjust Sharpness", 0.0, 3.0, 1.0, 0.1)
        sharpness_enhancer = ImageEnhance.Sharpness(image)
        sharp_image = sharpness_enhancer.enhance(sharpness_factor)
        if st.button("Apply Sharpness"):
            st.image(sharp_image, caption="Sharpness Adjusted Image", use_container_width=True)

        contrast_factor = st.slider("Adjust Contrast", 0.0, 3.0, 1.0, 0.1)
        contrast_enhancer = ImageEnhance.Contrast(image)
        contrast_image = contrast_enhancer.enhance(contrast_factor)
        if st.button("Apply Contrast"):
            st.image(contrast_image, caption="Contrast Adjusted Image", use_container_width=True)

        brightness_factor = st.slider("Adjust Brightness", 0.0, 3.0, 1.0, 0.1)
        brightness_enhancer = ImageEnhance.Brightness(image)
        brightness_image = brightness_enhancer.enhance(brightness_factor)
        if st.button("Apply Brightness"):
            st.image(brightness_image, caption="Brightness Adjusted Image", use_container_width=True)

        color_factor = st.slider("Adjust Color", 0.0, 3.0, 1.0, 0.1)
        color_enhancer = ImageEnhance.Color(image)
        color_image = color_enhancer.enhance(color_factor)
        if st.button("Apply Color Adjustment"):
            st.image(color_image, caption="Color Adjusted Image", use_container_width=True)

        if st.button("Apply Edge Enhancement"):
            edge_image = image.filter(ImageFilter.EDGE_ENHANCE)
            st.image(edge_image, caption="Edge Enhanced Image", use_container_width=True)

        if st.button("Apply Emboss"):
            emboss_image = image.filter(ImageFilter.EMBOSS)
            st.image(emboss_image, caption="Embossed Image", use_container_width=True)

        if st.button("Apply Contour"):
            contour_image = image.filter(ImageFilter.CONTOUR)
            st.image(contour_image, caption="Contoured Image", use_container_width=True)

        blur_radius = st.slider("Adjust Gaussian Blur Radius", 0.0, 10.0, 1.0, 0.1)
        if st.button("Apply Gaussian Blur"):
            gaussian_blur_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
            st.image(gaussian_blur_image, caption="Gaussian Blurred Image", use_container_width=True)

        if st.button("Apply Negative"):
            negative_image = Image.eval(image, lambda x: 255 - x)
            st.image(negative_image, caption="Negative Image", use_container_width=True)
            buffer = BytesIO()
            negative_image.save(buffer, format="JPEG")
        
        if st.button("Apply Sobel Edge Detection"):
            image_array = np.array(image.convert("L"))  # Convert to grayscale
            sobel_x = cv2.Sobel(image_array, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(image_array, cv2.CV_64F, 0, 1, ksize=3)
            sobel_edge = cv2.magnitude(sobel_x, sobel_y)
            sobel_edge = np.uint8(sobel_edge / sobel_edge.max() * 255)
            st.image(sobel_edge, caption="Sobel Edge Detection", use_container_width=True, channels="GRAY")
            buffer = BytesIO()
            edge_image = Image.fromarray(sobel_edge)
            edge_image.save(buffer, format="JPEG")

        threshold_value = st.slider("Select Threshold Value", min_value=0, max_value=255, value=128)
        if st.button("Apply Thresholding"):
            image_array = np.array(image.convert("L"))  # Convert to grayscale
            _, threshold_image = cv2.threshold(image_array, threshold_value, 255, cv2.THRESH_BINARY)
            st.image(threshold_image, caption="Thresholded Image", use_container_width=True, channels="GRAY")

        if st.button("Apply Sepia"):
            sepia_filter = np.array([[0.393, 0.769, 0.189],
                                     [0.349, 0.686, 0.168],
                                     [0.272, 0.534, 0.131]])
            image_array = np.array(image)
            sepia_image = cv2.transform(image_array, sepia_filter)
            sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)
            st.image(sepia_image, caption="Sepia Image", use_container_width=True)

elif menu == "Meet the Members":
            # Title - Centered
            st.markdown(
                "<h1 style='text-align: center;'>Meet the Members of Group 8</h1>",
                unsafe_allow_html=True
            )
            
            # Centered layout for each member using HTML and CSS
            st.markdown(
                """
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/ahmadfaqihy/WebAppGroup8/refs/heads/master/3.png" width="300">
                    <h4>Ahmad Faqih Yassin</h4>
                    <p>Role: Team Leader</p>
                    <p>004202305045</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown(
                """
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/ahmadfaqihy/WebAppGroup8/refs/heads/master/2.png" width="300">
                    <h4>Miftakhul Adam</h4>
                    <p>004202305068</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown(
                """
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/ahmadfaqihy/WebAppGroup8/refs/heads/master/1.png" width="300">
                    <h4>Ridho Alhabsy</h4>
                    <p>004202305068</p>
                </div>
                """,
                unsafe_allow_html=True
            )
