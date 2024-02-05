## PILLOW IMAGE PROCESSING APP WITH STREAMLIT

# image_process.py

import streamlit as st
from PIL import Image, ImageFilter
from blur import blur
from detail import detail
from sharp import enhance_sharpness
from color import adjust_color 

def main():
    st.title('Pillow Image Processing App With Streamlit')
    st.markdown("Welcome to the Image Processing Demo! Upload an image and explore various image processing techniques.")


    # Your main app content goes here...

    st.header("Image Filtering,Blurring,Detail Enhancement, Adjusting Image Color and sharpness")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        ### Blur image
        st.subheader("The Blur Image Filter")       
        st.markdown('Click the "Blur Image" button to apply a blur effect to the uploaded image.')

        # Process image on button click
        if st.button("Blur Image"):
            input_image = Image.open(uploaded_file)
            output_image_path = "blurred_image.jpg"
            blur(input_image, output_image_path)
            st.image(output_image_path, caption="Blurred Image", use_column_width=True)
            st.success("Blurring image complete!")

        ### Detail Enhancement
        st.subheader("The Detail Enhancement Filter") 
        st.markdown('Ajust the Detail Enhancement factor and Click the "Enhance Detail" button to improve the image details. This function uses image filters to enhance fine details.')
        
        # Slider for enhancing sharpness
        enhance_factor = st.slider("Select Detail Enhancement Factor", 1.0, 3.0, 1.0, 0.1)

        # Process image on button click
        if st.button("Enhance Detail"):
            input_image = Image.open(uploaded_file)
            output_image_path = "detailed_image.jpg"
            detail(input_image, output_image_path)
            st.image(output_image_path, caption="Enhanced Image", use_column_width=True)
            st.success("Detail enhancement complete!")

        ### Image Sharpness Enhancement
        st.subheader("The Image Sharpness Enhancement Filter")             
        st.markdown('Adjust the sharpness of the image using the "Enhance Sharpness" slider. Experiment with different sharpness enhancement factors and click "Enhance Sharpness" to apply the changes.')
        
       
        # Slider for enhancing sharpness
        enhance_factor = st.slider("Select Sharpness Enhancement Factor", 1.0, 3.0, 1.0, 0.1)
         # Process image on button click
        if st.button("Enhance Sharpness"):
            input_image = Image.open(uploaded_file)
            output_image_path = "sharpened_image.jpg"  # You can customize the output path
            enhance_sharpness(input_image, enhance_factor, output_image_path)
            st.image(output_image_path, caption="Sharpened Image", use_column_width=True)
            st.success("Sharpness enhancement complete!")

        ### Image Color Enhancement
        st.subheader("The Image Color Enhancement Filter")  
        st.markdown('Use the sliders to dynamically adjust the brightness, contrast, and saturation of the image. Click "Adjust Color" to apply the changes.')   
        # Sliders for color enhancement
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



