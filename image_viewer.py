# image_viewer.py

import streamlit as st
import io
import os
from PIL import Image

def main():
    st.title("(a) Image Viewer")
    st.markdown('In this Demo, you will be able to view images from your device!') 

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image.thumbnail((400, 400))
        st.image(image, caption="Uploaded Image", use_column_width=True)

if __name__ == "__main__":
    main()