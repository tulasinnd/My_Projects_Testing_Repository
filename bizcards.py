import streamlit as st
import easyocr
import cv2
import numpy as np

st.set_page_config(page_title='Text Blocks Detection with EasyOCR')
st.title('Text Blocks Detection with EasyOCR')
st.write('Upload an image and the app will detect the text blocks in it.')
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    reader = easyocr.Reader(['en'])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    text_blocks = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        roi = image[y:y + h, x:x + w]
        results = reader.readtext(roi)
        if results:
            text = [result[1] for result in results]
            text_blocks.append((text, [x, y, x + w, y + h]))
    for i, block in enumerate(text_blocks):
        st.write(f'Text Block {i+1}:\nText: {block[0]}\nBounding Box: {block[1]}')
