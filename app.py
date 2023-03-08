import cv2
import numpy as np
import streamlit as st

# Set up Streamlit app
st.set_page_config(page_title="Image Text Block Margins", layout="wide")
st.title("Image Text Block Margins")

# Upload image file
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Display image with text block margins
if uploaded_file is not None:
    # Read image file as numpy array
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to remove noise
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours in the image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours and draw bounding boxes around text blocks
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 50 and h > 50:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the new image with bounding boxes around text blocks
    st.image(img, channels="BGR")
else:
    st.warning("Please upload an image file.")
