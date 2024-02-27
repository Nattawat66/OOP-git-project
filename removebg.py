from io import BytesIO
import streamlit as st
from PIL import Image, ImageEnhance
from rembg import remove
import base64

def set_background(image_url):
    image_url_str = f'url("{image_url}")'
    css = f"""
    <style>
    .stApp {{
        background-image: {image_url_str};
        background-size: cover;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


##ใช้งานตรงนี้
set_background("https://wallpapers.com/images/hd/minimalist-earth-and-moon-ol93aaxwrqhygnb9.jpg")

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

st.title("Background Remover")
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "png"])

if uploaded_image is not None:
    original_image = Image.open(uploaded_image)
    original_width, original_height = original_image.size
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("Original Image")
        st.image(original_image, caption="Uploaded Image", use_column_width=True)
        selected_format = st.selectbox("Select Download Format", ["PNG", "JPG"])

    if st.button("Remove Background"):
        
        with col2:
            fixed = remove(original_image)
            st.header("Remove BG Image")
            st.image(fixed, caption="Processed Image", use_column_width=True)
            downloadable_image = convert_image(fixed)
            if selected_format == "PNG":
                st.download_button(
                    "Download Image", downloadable_image, "removebg.png", "image/png", key="download_button_1"
                )
            elif selected_format == "JPG":
                st.download_button(
                    "Download Image", downloadable_image, "removebg.jpg", "image/jpeg", key="download_button_2"
                )
            print("56")    
                

