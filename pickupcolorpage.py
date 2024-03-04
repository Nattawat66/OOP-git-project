import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
from matplotlib.colors import to_hex
from streamlit_image_coordinates import streamlit_image_coordinates

# อัปโหลดรูปภาพ

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def show_color_swatch(color):
  # แปลงค่า RGB เป็น Hex

  # สร้าง HTML code สำหรับตัวอย่างสี
  html_code = f"""
  <div style="width: 150px; height: 150px; background-color: {color}; border: 1px solid black; margin: 10px;">
    
  </div>
  """

  # แสดงตัวอย่างสี
  st.write(html_code, unsafe_allow_html=True)


def show():

    # แสดงรูปภาพ
    st.title("Picker Color")
    uploaded_file = st.file_uploader("อัปโหลดรูปภาพ")

    if uploaded_file is not None:
        original_image = Image.open(uploaded_file)

        # เก็บขนาดรูปภาพดั้งเดิม
        width, height = original_image.size

        # ปรับขนาดรูปภาพให้เหมาะสมกับหน้าจอ
        max_width = 800
        if width > max_width:
            original_image = original_image.resize((max_width, int(height * (max_width / width))))


        # เลือกสีจากรูปภาพ
        value = streamlit_image_coordinates(original_image)
        # แสดงค่าสี RGB
        if value is None:
            st.header("ใช้เมาส์ของคุณคลิ๊กที่ตำแหน่งสีที่ต้องการบนรูปภาพ")

        if value is not None:
            x = int(value['x'])
            y = int(value['y'])
            # ดึงค่าสีจากภาพตามตำแหน่งที่เลือก
            image_array = np.array(original_image)
            color = image_array[y, x]
            show_color_swatch(rgb_to_hex(color[0],color[1],color[2]))
            st.title(f"ค่าสี: Hex: {rgb_to_hex(color[0],color[1],color[2])}")
            st.title(f"ค่าสี: RGB: ({color[0]}, {color[1]}, {color[2]})")
            



