import cv2
import pytesseract
import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Text Recognition", page_icon=":pencil:", layout="wide")

# Define Tesseract configuration options
config = '--psm 6'

# Define Streamlit app
st.title("Text Recognition")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image and convert to grayscale
    image = Image.open(uploaded_file)
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binarize the image using adaptive thresholding
    binarized = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, blockSize=15, C=5)

    # Find contours in the binarized image
    contours, hierarchy = cv2.findContours(binarized, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour and find text blocks
    text_blocks = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 100 and h > 10:
            # Crop the text block from the original image
            block = img[y:y+h, x:x+w]
            text_blocks.append(block)

    # Apply OCR to each text block and print the recognized text and text block image
    for i, block in enumerate(text_blocks):



        # Convert the image to a NumPy array
        numpy_array = np.array(block)

        # Convert the image to a PIL image
        pil_image = Image.fromarray(numpy_array)

        text = pytesseract.image_to_string(pil_image, config=config)
        st.write(f"Text Block {i+1}: {text}")
        st.image(block, caption=f"Text Block {i+1} Image", use_column_width=True)
