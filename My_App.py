import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
st. set_page_config(layout="wide")
import re

#title
st.title("EXTRACTING TEXT FROM IMAGES USING OCR")
st.write(" ")
st.write(" ")
col1, col2,col3 = st.columns([2,4,2])
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
    with col1:
        #st.write("## YOUR IMAGE")
        st.image(input_image) #display image        
    
    result = reader.readtext(np.array(input_image))
    result_text = [] #empty list for results
    for text in result:
        result_text.append(text[1])
      
    with col3:
        st.write("## UPLOAD OR DELETE")
        if st.button('UPLOAD'):
            st.write('WRITE CODE FOR UPLOAD')
    
    PH=[]
    PHID=[]  
    ADD=set()
    AID=[]
    EMAIL=''
    EID=''
    PIN=''
    PID=''
    WEB=''
    WID=''
    
    for i, string in enumerate(result_text):   
        st.write(string.lower())     
        
        # TO FIND EMAIL
        if re.search(r'@', string.lower()):
            EMAIL=string.lower()
            EID=i
        
        # TO FIND PINCODE
        match = re.search(r'\d{6,7}', string.lower())
        if match:
            PIN=match.group()
            PID=i
                       
        # TO FIND PHONE NUMBER    
        match = re.search(r'(?:ph|phone|phno)?(?:[+-]?\d*){7,}', string)
        if match and len(re.findall(r'\d', string)) > 7:
            PH.append(match.group())
            PHID.append(i)
            
        # TO FIND ADDRESS 
        keywords = ['road', 'floor', ' st ', 'st,', 'street', ' dt ', 'district', 'near', 'beside', 'opposite', ' at ', ' in ', 'center', 'main road', '2nd', '3rd']
        # Define the regular expression pattern to match six or seven continuous digits
        digit_pattern = r'\d{6,7}'
        # Check if the string contains any of the keywords or a sequence of six or seven digits
        if any(keyword in string.lower() for keyword in keywords) or re.search(digit_pattern, string):
            ADD.add(string)
            AID.append(i)
            
        # TO FIND STATE (USING SIMILARITY SCORE)
        states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 
          'Haryana','Hyderabad', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh',
            'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 
            'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
        import Levenshtein
        def string_similarity(s1, s2):
            distance = Levenshtein.distance(s1, s2)
            similarity = 1 - (distance / max(len(s1), len(s2)))
            return similarity * 100
        
        for x in states:
            similarity = string_similarity(x.lower(), string.lower())
            if similarity > 50:
                ADD.add(string)
                AID.append(i)
                
        # WEBSITE URL          
        if re.match(r"(?!.*@)(www|.*com$)", string):
            WEB=string.lower()
            WID=i 
    with col2: 
        st.write('#### WEBSITE URL'+ str(WEB))
        st.write('#### :red[EMAIL: ]'+ str(EMAIL)) 
        st.write('#### :red[PIN CODE: ]'+ str(PIN)) 
        st.write('PHONE NUMBER(S)', PH)
        st.write('ADDRESS', ADD)


        IDS= [EID,PID,WID]
        IDS.extend(AID)
        IDS.extend(PHID)
#         st.write(IDS)

        st.write('OTHER DETAILS')
        for i, string in enumerate(result_text):
            if i not in IDS:            
                st.write(string)
    
    

        
            
#     import en_core_web_sm
#     nlp = en_core_web_sm.load()
#     import spacy
            
#     str1 = ""   
#     for ele in result_text:    
#         str1 += ele+" "
# #     doc= nlp(str1)
# #     for ent in doc.ents:
# #         st.write(ent.text,'| ', ent.label_, '| ', spacy.explain(ent.label_))
        
#     import re

#     # Regular expression for email addresses
#     email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#     # Regular expression for phone numbers
#     phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
#     # Regular expression for pin codes
#     pincode_pattern = r'\b\d{6}\b'

#     # Find all email addresses, phone numbers, website URLs, and pin codes in the string using regex
#     emails = re.findall(email_pattern, str1)
#     phone_numbers = re.findall(phone_pattern, str1)
#     pincodes = re.findall(pincode_pattern, str1)

#     # Print the results
#     st.write("DETAILS")
#     st.write("Email addresses:", emails)
#     st.write("Phone numbers:", phone_numbers)
# #     st.write("Website URLs:", urls)
#     st.write("Pin codes:", pincodes)
    

#     # Find all words that start with "www" (case-insensitive) and do not contain "@"
#     matches = re.findall(r"\bwww(?!\S*@)\S*\b", str1, re.IGNORECASE)

#     # Process each match
#     for match in matches:
#         # Remove extra spaces
#         match = " ".join(match.split())

#         # Convert to lowercase
#         match = match.lower()

#         # Add "." after "www" if not present
#         if not match.startswith("www."):
#             match = "www." + match[len("www"):]

#         # Add "." before "com" if not present
#         if not match.endswith(".com"):
#             match = match[:len(match) - len(".com")] + ".com"

#         st.write(match)



        

    
    
        
   
