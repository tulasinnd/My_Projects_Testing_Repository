import streamlit as st
import easyocr
import cv2
import numpy as np

# Define a function to get the bounding boxes and text from an image
def get_bounding_boxes():
        # Set the page title
    st.set_page_config(page_title='Text Detection with EasyOCR')
    
    # Add a title and description to the app
    st.title('Text Detection with EasyOCR')
    st.write('Upload an image and the app will detect the text in it.')
    
    # Add a file uploader to the app
    uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
    
    # If an image is uploaded, display it and the text in it
    if uploaded_file is not None:
        # Read the image from the file
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        
    
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'])
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to the image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    # Get the contours of the text regions in the image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate over the contours and get the bounding boxes and text for each one
    boxes = []
    for contour in contours:
        # Get the bounding box for the contour
        (x, y, w, h) = cv2.boundingRect(contour)
        
        # Crop the region of interest (ROI) from the image
        roi = image[y:y + h, x:x + w]
        
        # Use EasyOCR to read the text in the ROI
        results = reader.readtext(roi)
        
        # Append the bounding box and text to the list of boxes
        st.write(results[0][1])
        
#     # Display the image with the bounding boxes and text
#         st.image(image, channels='BGR', caption='Original Image')
#         for i, box in enumerate(boxes):
#             st.write(f'Text {i+1}: {box[1]}')
#             image = cv2.rectangle(image, (box[0][0], box[0][1]), (box[0][2], box[0][3]), (0, 255, 0), 2)
#         st.image(image, channels='BGR', caption='Image with Text Detection')
 

# Define the Streamlit app
def main():
    get_bounding_boxes()
            
# Run the app
if __name__ == '__main__':
    main()
