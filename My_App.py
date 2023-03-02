import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
st. set_page_config(layout="wide")

#title
st.title("EXTRACTING TEXT FROM IMAGES USING OCR")
st.write(" ")
st.write(" ")
col1, col2,col3,col4 = st.columns([2,2,2,2])
with col1:
    #image uploader
    st.write("## UPLOAD IMAGE")
    image = st.file_uploader(label = "",type=['png','jpg','jpeg'])

@st.cache
def load_model(): 
    reader = ocr.Reader(['en'])#,model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:
    input_image = Image.open(image) #read image
    with col2:
        st.write("## YOUR IMAGE")
        st.image(input_image) #display image        
    
    result = reader.readtext(np.array(input_image))
    result_text = [] #empty list for results
    for text in result:
        result_text.append(text[1])
        
# company name, 
# card holder name, 
# designation, 
# mobile number, 
# email address, 
# website URL, 
# area, 
# city, 
# state,
# pin code

    with col3:
        st.write("## EXTRACTED TEXT")
        for i in result_text:
            st.write(i)
    with col4:
        st.write("## UPLOAD OR DELETE")
        if st.button('UPLOAD'):
            st.write('WRITE CODE FOR UPLOAD')
            
str1 = ""
   
for ele in result_text:    
    str1 += ele

import spacy
nlp = spacy.load('en_core_web_sm')
doc= nlp(str1)

for ent in doc.ents:
    st.write(ent.text,'|', ent.label_)
 




