import streamlit as st
from removebgpage import main as remove_page
from pickupcolorpage import main as pickupcolor_page

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
def hide_bar():
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_st_style, unsafe_allow_html=True)    

def main():
    #hide_bar()    
    set_background("https://wallpaper.dog/large/20474170.jpg")

    st.sidebar.title("Menu")
    selection = st.sidebar.radio("Go to", ["RemoveBackgound","PickUpColor"])

    if selection == "RemoveBackgound":
        remove_page()
    elif selection == "PickUpColor":
        pickupcolor_page()



if __name__ == "__main__":
    main()