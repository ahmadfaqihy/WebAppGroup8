import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
from io import BytesIO

# Sidebar navigation
menu = st.sidebar.selectbox("Select Page", ["Home", "Apply Filter", "Meet the Members"])

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
            <p>Explore various capability to alter your image using the application of Image Processing with Linear Algebra Principle:</p>
            <ul style="text-align: left;">
                <li>Upload and process your images</li>
                <li>Convert to grayscale, blur, sepia tone, contour, sharpness adjustment, and many more!</li>
                <li>Download the processed images</li>
            </ul>
            <p>Use the sidebar to navigate to the application!</p>
            <p>Group 8 - N IE 01</p>
            <p>Industrial Engineering - Faculty of Engineering</p>
            <p>President University</p>
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

        # Sharpness Filter
        sharpness_factor = st.slider("Adjust Sharpness", 0.0, 3.0, 1.0, 0.1)
        sharpness_enhancer = ImageEnhance.Sharpness(image)
        sharp_image = sharpness_enhancer.enhance(sharpness_factor)
        if st.button("Apply Sharpness"):
            st.image(sharp_image, caption="Sharpness Adjusted Image", use_container_width=True)

        # Contrast Filter
        contrast_factor = st.slider("Adjust Contrast", 0.0, 3.0, 1.0, 0.1)
        contrast_enhancer = ImageEnhance.Contrast(image)
        contrast_image = contrast_enhancer.enhance(contrast_factor)
        if st.button("Apply Contrast"):
            st.image(contrast_image, caption="Contrast Adjusted Image", use_container_width=True)

        # Brightness Filter
        brightness_factor = st.slider("Adjust Brightness", 0.0, 3.0, 1.0, 0.1)
        brightness_enhancer = ImageEnhance.Brightness(image)
        brightness_image = brightness_enhancer.enhance(brightness_factor)
        if st.button("Apply Brightness"):
            st.image(brightness_image, caption="Brightness Adjusted Image", use_container_width=True)

        # Color Filter
        color_factor = st.slider("Adjust Color", 0.0, 3.0, 1.0, 0.1)
        color_enhancer = ImageEnhance.Color(image)
        color_image = color_enhancer.enhance(color_factor)
        if st.button("Apply Color Adjustment"):
            st.image(color_image, caption="Color Adjusted Image", use_container_width=True)

        # Edge Enhancement Filter
        if st.button("Apply Edge Enhancement"):
            edge_image = image.filter(ImageFilter.EDGE_ENHANCE)
            st.image(edge_image, caption="Edge Enhanced Image", use_container_width=True)

        # Emboss Filter
        if st.button("Apply Emboss"):
            emboss_image = image.filter(ImageFilter.EMBOSS)
            st.image(emboss_image, caption="Embossed Image", use_container_width=True)

        # Contour Filter
        if st.button("Apply Contour"):
            contour_image = image.filter(ImageFilter.CONTOUR)
            st.image(contour_image, caption="Contoured Image", use_container_width=True)

        # Gaussian Blur Filter
        blur_radius = st.slider("Adjust Gaussian Blur Radius", 0.0, 10.0, 1.0, 0.1)
        if st.button("Apply Gaussian Blur"):
            gaussian_blur_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
            st.image(gaussian_blur_image, caption="Gaussian Blurred Image", use_container_width=True)

elif menu == "Meet the Members":
    st.title("Meet the Members of Group 8")
    st.markdown("### Member 1")
    st.image("https://via.placeholder.com/150", caption="Member 1 Name")
    st.write("Role: Team Leader")
    st.write("Description: Brief description about Member 1.")

    st.markdown("### Member 2")
    st.image("https://via.placeholder.com/150", caption="Member 2 Name")
    st.write("Role: Developer")
    st.write("Description: Brief description about Member 2.")

    st.markdown("### Member 3")
    st.image("https://via.placeholder.com/150", caption="Member 3 Name")
    st.write("Role: Designer")
    st.write("Description: Brief description about Member 3.")
