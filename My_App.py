import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
st. set_page_config(layout="wide")

#title
st.title("EXTRACTING TEXT FROM IMAGES USING OCR")

col1, col2,col3 = st.columns([2.5,2.5,5])
with col1:
    #image uploader
    image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

@st.cache
def load_model(): 
    reader = ocr.Reader(['en'])#,model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:
    input_image = Image.open(image) #read image
    with col2:
        st.image(input_image) #display image        
    
    result = reader.readtext(np.array(input_image))
    result_text = [] #empty list for results
    for text in result:
        result_text.append(text[1])
        
    with col3:
        for i in result_text:
            st.write(i)




