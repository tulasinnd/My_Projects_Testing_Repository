import streamlit as st
import cv2
import pytesseract
import numpy as np

st.title("Extract Text from Images")

# Allow user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to remove noise
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilation to make text regions more visible
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=5)

    # Get the contours of the text regions
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour and crop the text region
    for i, contour in enumerate(contours):
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Crop the text region from the original image
        cropped_img = img[y:y+h, x:x+w]

        # Apply OCR to the cropped image
        text = pytesseract.image_to_string(cropped_img, lang='eng')

        # Display the cropped image and its corresponding text
        st.image(cropped_img, caption=f'Text {i+1}: {text}', use_column_width=True)
