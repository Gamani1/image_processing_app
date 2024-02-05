# detail_image.py

import streamlit as st
from PIL import Image, ImageFilter
import io

def detail(input_image, output_image):
    if isinstance(input_image, Image.Image):
        # If the input_image is already an Image object, use it directly
        image = input_image
    else:
        # Otherwise, assume it's a file-like object and open it
        image = Image.open(io.BytesIO(input_image.read()))

    filtered_image = image.filter(ImageFilter.DETAIL)
    filtered_image.save(output_image)

def main():
    st.title('Image Detail Enhancement ')
    st.markdown('In this Demo, you will enhance the quality of your image by uploading it.')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Process image on button click
        if st.button("Enhance Detail"):
            input_image = uploaded_file
            output_image_path = "detailed_image.jpg"

            detail(input_image, output_image_path)

            st.image(output_image_path, caption="Enhanced Image", use_column_width=True)
            st.success("Detail enhancement complete!")

if __name__ == "__main__":
    main()
