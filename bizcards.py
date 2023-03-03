import streamlit as st
import easyocr
from PIL import Image

st.title("Business Card Reader")

# Upload the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Extract text from the image using EasyOCR
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)

    # Display the extracted information
    company_name = ''
    card_holder_name = ''
    designation = ''
    mobile_number = ''
    email_address = ''
    website_url = ''
    area = ''
    city = ''
    state = ''
    pin_code = ''
    for r in result:
        if 'company' in r[1].lower():
            company_name = r[0]
        elif 'name' in r[1].lower() and 'holder' in r[1].lower():
            card_holder_name = r[0]
        elif 'designation' in r[1].lower():
            designation = r[0]
        elif 'mobile' in r[1].lower() or 'phone' in r[1].lower():
            mobile_number = r[0]
        elif 'email' in r[1].lower():
            email_address = r[0]
        elif 'website' in r[1].lower():
            website_url = r[0]
        elif 'area' in r[1].lower():
            area = r[0]
        elif 'city' in r[1].lower():
            city = r[0]
        elif 'state' in r[1].lower():
            state = r[0]
        elif 'pin' in r[1].lower() or 'code' in r[1].lower():
            pin_code = r[0]

    st.write("## Extracted Information")
    st.write(f"**Company Name:** {company_name}")
    st.write(f"**Card Holder Name:** {card_holder_name}")
    st.write(f"**Designation:** {designation}")
    st.write(f"**Mobile Number:** {mobile_number}")
    st.write(f"**Email Address:** {email_address}")
    st.write(f"**Website URL:** {website_url}")
    st.write(f"**Area:** {area}")
    st.write(f"**City:** {city}")
    st.write(f"**State:** {state}")
    st.write(f"**Pin Code:** {pin_code}")
