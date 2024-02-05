# enhance_sharpness.py

import streamlit as st
from PIL import Image, ImageEnhance

def enhance_sharpness(image, enhance_factor, output_path):
    enhancer = ImageEnhance.Sharpness(image)
    new_image = enhancer.enhance(enhance_factor)
    new_image.save(output_path)

def main():
    st.title('Image Sharpness Enhancement with Streamlit')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Slider for enhancing sharpness
        enhance_factor = st.slider("Select Sharpness Enhancement Factor", 1.0, 3.0, 1.0, 0.1)

        # Process image on button click
        if st.button("Enhance Sharpness"):
            input_image = Image.open(uploaded_file)
            output_image_path = "sharpened_image.jpg"  

            enhance_sharpness(input_image, enhance_factor, output_image_path)

            st.image(output_image_path, caption="Sharpened Image", use_column_width=True)
            st.success("Sharpness enhancement complete!")

if __name__ == "__main__":
    main()
