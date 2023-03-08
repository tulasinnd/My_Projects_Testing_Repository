import streamlit as st
import cv2
import numpy as np
import pytesseract
from google.cloud import vision
from google.cloud.vision_v1.types import Image

# Authenticate with Google Cloud Vision API
client = vision.ImageAnnotatorClient()

# Set up Streamlit app
st.set_page_config(page_title="Image Text Recognition", page_icon=":camera:")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to remove noise
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilation to merge text into single blocks
    kernel = np.ones((5,5), np.uint8)
    dilation = cv2.dilate(thresh, kernel, iterations=5)

    # Detect text blocks using Google Cloud Vision API
    image = Image(content=cv2.imencode('.jpg', dilation)[1].tostring())
    response = client.document_text_detection(image=image)
    blocks = response.full_text_annotation.pages[0].blocks

    # Draw text blocks on image
    for block in blocks:
        for paragraph in block.paragraphs:
            for word in paragraph.words:
                for symbol in word.symbols:
                    vertices = symbol.bounding_box.vertices
                    cv2.rectangle(img, (vertices[0].x, vertices[0].y), (vertices[2].x, vertices[2].y), (0, 255, 0), 2)

    # Display image
    st.image(img, caption="Processed image with text blocks", use_column_width=True)
