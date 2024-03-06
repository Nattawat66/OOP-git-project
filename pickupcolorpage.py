import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
from streamlit_image_coordinates import streamlit_image_coordinates

# อัปโหลดรูปภาพ

class PickerColor:
  def __init__(self):
    self.original_image = None
    self.width = None
    self.height = None

  def rgb_to_hex(self, r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

  def showcolor(self, color):
    html_code = f"""
    <div style="width: 150px; height: 150px; background-color: {color}; border: 1px solid black; margin: 10px;">
    </div>
    """
    st.write(html_code, unsafe_allow_html=True)

  def main(self):
    st.title("Picker Color")
    uploaded_file = st.file_uploader("อัปโหลดรูปภาพ")

    if uploaded_file is not None:
      self.original_image = Image.open(uploaded_file)
      self.width, self.height = self.original_image.size

      max_width = 800
      if self.width > max_width:
        self.original_image = self.original_image.resize((max_width, int(self.height * (max_width / self.width))))

      value = streamlit_image_coordinates(self.original_image)

      if value is None:
        st.header("ใช้เมาส์ของคุณคลิ๊กที่ตำแหน่งสีที่ต้องการบนรูปภาพ")

      if value is not None:
        x = int(value['x'])
        y = int(value['y'])

        image_array = np.array(self.original_image)
        color = image_array[y, x]

        self.showcolor(self.rgb_to_hex(color[0], color[1], color[2]))
        st.title(f"ค่าสี: Hex: {self.rgb_to_hex(color[0], color[1], color[2])}")
        st.title(f"ค่าสี: RGB: ({color[0]}, {color[1]}, {color[2]})")

# เรียกใช้งาน class
def main():
    picker_color = PickerColor()
    picker_color.main()
