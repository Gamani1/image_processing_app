# color_enhancement_streamlit.py

import streamlit as st
from PIL import Image, ImageEnhance

def adjust_color(image, brightness_factor, contrast_factor, saturation_factor, output_path):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)

    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(saturation_factor)

    image.save(output_path)

def main():
    st.title('Color Enhancement with Streamlit')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Sliders for adjusting color
        brightness_factor = st.slider("Adjust Brightness", 0.1, 2.0, 1.0, 0.1)
        contrast_factor = st.slider("Adjust Contrast", 0.1, 2.0, 1.0, 0.1)
        saturation_factor = st.slider("Adjust Saturation", 0.1, 2.0, 1.0, 0.1)

        # Process image on button click
        if st.button("Adjust Color"):
            input_image = Image.open(uploaded_file)
            output_image_path = "color_adjusted_image.jpg"  
            adjust_color(input_image, brightness_factor, contrast_factor, saturation_factor, output_image_path)
            st.image(output_image_path, caption="Color Adjusted Image", use_column_width=True)
            st.success("Color adjustment complete!")

if __name__ == "__main__":
    main()
