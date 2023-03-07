import streamlit as st
import easyocr
import cv2
import numpy as np

st.set_page_config(page_title='Text Detection with EasyOCR')
st.title('Text Detection with EasyOCR')
st.write('Upload an image and the app will detect the text in it.')
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    reader = easyocr.Reader(['en'])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        roi = image[y:y + h, x:x + w]
        results = reader.readtext(roi)
        st.write([results[0][1]])
    for i, box in enumerate(boxes):
        st.write(f'Text {i+1}: {box[1]}')
