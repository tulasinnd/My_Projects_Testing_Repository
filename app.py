import cv2
import numpy as np
import streamlit as st

# Set up Streamlit app
st.set_page_config(page_title="Image Text Block Margins", layout="wide")
st.title("Image Text Block Margins")

# Upload image file
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Define default thresholding parameters
default_thresh_val = 127
default_thresh_type = "Binary"
default_thresh_mode = "OTSU"

# Define Streamlit sliders for adjusting thresholding parameters
thresh_val = st.slider("Threshold value", min_value=0, max_value=255, value=default_thresh_val)
thresh_type = st.selectbox("Threshold type", options=["Binary", "Binary Inv"], index=0)
thresh_mode = st.selectbox("Threshold mode", options=["OTSU", "Adaptive"], index=0)
block_size = st.slider("Block size (for adaptive thresholding)", min_value=3, max_value=99, value=11, step=2)

# Display image with text block margins
if uploaded_file is not None:
    # Read image file as numpy array
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply pre-processing to reduce noise and improve text recognition
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply thresholding to remove noise
    if thresh_mode == "OTSU":
        thresh_mode_flag = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    else:
        thresh_mode_flag = cv2.THRESH_BINARY_INV
    if thresh_type == "Binary":
        thresh_type_flag = cv2.THRESH_BINARY
    else:
        thresh_type_flag = cv2.THRESH_BINARY_INV
    if thresh_mode == "Adaptive":
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresh_type_flag, block_size, 2)
    else:
        _, thresh = cv2.threshold(gray, thresh_val, 255, thresh_type_flag + thresh_mode_flag)

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
