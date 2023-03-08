import streamlit as st
import pytesseract
import easyocr
from PIL import Image

st.title("Image Text Extraction")

# Select image
img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if img_file_buffer is not None:
    # Load image
    img = Image.open(img_file_buffer)

    # Display image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Extract text using EasyOCR
    reader = easyocr.Reader(['en'])
    text = reader.readtext(img)

    # Extract text using Pytesseract
    # text = pytesseract.image_to_string(img)

    # Display extracted text
    st.write("Extracted Text:")
    for i in text:
        st.write(i[1])
