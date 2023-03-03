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
        
    with col3:
        st.write("## EXTRACTED TEXT")
        for i in result_text:
            st.write(i)
    with col4:
        st.write("## UPLOAD OR DELETE")
        if st.button('UPLOAD'):
            st.write('WRITE CODE FOR UPLOAD')
    import en_core_web_sm
    nlp = en_core_web_sm.load()
    import spacy
            
    str1 = ""
   
    for ele in result_text:    
        str1 += ele+" "

    doc= nlp(str1)

    for ent in doc.ents:
        st.write(ent.text,'| ', ent.label_, '| ', spacy.explain(ent.label_))
        
    import re

    # Regular expression for email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Regular expression for phone numbers
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

    # Regular expression for website URLs
    url_pattern = r"www\.\w+\.com"

    # Regular expression for pin codes
    pincode_pattern = r'\b\d{6}\b'

    # Find all email addresses, phone numbers, website URLs, and pin codes in the string using regex
    emails = re.findall(email_pattern, str1)
    phone_numbers = re.findall(phone_pattern, str1)
    urls = re.findall(url_pattern, str1)
    pincodes = re.findall(pincode_pattern, str1)

    # Print the results
    st.write("DETAILS")
    st.write("Email addresses:", emails)
    st.write("Phone numbers:", phone_numbers)
    st.write("Website URLs:", urls)
    st.write("Pin codes:", pincodes)


        

    
    
        
   
