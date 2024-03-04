from io import BytesIO
import streamlit as st
from PIL import Image, ImageEnhance,ImageDraw
from rembg import remove
import base64


def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def show():
    
    st.title("Background Remover")
    uploaded_image = st.file_uploader("Upload Image",accept_multiple_files=True, type=["jpg", "png"])

    if uploaded_image is not None:
        for i, myimg in enumerate(uploaded_image):
            original_image = Image.open(myimg)
            original_width, original_height = original_image.size
            i += 1
            col1, col2,col3 = st.columns(3)
            with col1:
                st.header("Your Image")
                st.image(original_image, caption="Uploaded Image", use_column_width=True)
                with col2:
                    fixed = remove(original_image)
                    st.header("Remove BG")
                    st.image(fixed, caption="Processed Image", use_column_width=True)
                    selected_format = st.selectbox(f"Select Download Format Picture {i}", ["PNG", "JPG"])
                    downloadable_image = convert_image(fixed)
                    if selected_format == "PNG":
                        st.download_button(
                            f"Download Image {i}", downloadable_image, f"removebg{i}.png", "image/png", key=f"download_button_{i}"
                        )
                    elif selected_format == "JPG":
                        st.download_button(
                            f"Download Image {i}", downloadable_image, f"removebg{i}.jpg", "image/jpeg", key=f"download_button_{i}"
                        )
            with col3:
                fixed = remove(original_image)
                bg_color = st.color_picker(f"Choose Background Color{i}", "#ffffff")
                bg_image = Image.new("RGB", (original_width, original_height), bg_color)
                bg_image.paste(fixed, (0, 0), fixed)
                st.image(bg_image, caption="Background Color Applied", use_column_width=True)
                selected_format = st.selectbox(f"Select Download{i}", ["PNG", "JPG"])
                downloadable_image = convert_image(bg_image)
                if selected_format == "PNG":
                    st.download_button(
                        f"Download Image {i}", downloadable_image, f"removebg{i}.png", "image/png", key=f"download_button_{i}_color"
                    )
                elif selected_format == "JPG":
                    st.download_button(
                        f"Download Image {i}", downloadable_image, f"removebg{i}.jpg", "image/jpeg", key=f"download_button_{i}_color"
                    )  

