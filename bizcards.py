import streamlit as st
import easyocr
import cv2

# Function to get all the bounding boxes of the text in the image
def get_bounding_boxes(image):
    # Load the image
    img = cv2.imread(image)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply binary thresholding to the image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Get the contours of the text in the image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # Get the bounding boxes of the text in the image
    boxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        boxes.append((x, y, x + w, y + h))
    return boxes

# Function to extract text from each bounding box
def extract_text(image, boxes):
    # Load the image
    img = cv2.imread(image)
    # Create an EasyOCR reader
    reader = easyocr.Reader(['en'], gpu=False)
    # Extract text from each bounding box
    texts = []
    for box in boxes:
        cropped_img = img[box[1]:box[3], box[0]:box[2]]
        text = reader.readtext(cropped_img)
        texts.append(text)
    return texts

# Main function to run the app
def main():
    st.set_page_config(page_title="OCR Bounding Box Extractor", page_icon=":books:")

    # Set up the sidebar
    st.sidebar.title("OCR Bounding Box Extractor")
    image = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if not image:
        st.warning("Please upload an image.")
        return

    # Process the image
    boxes = get_bounding_boxes(image)
    text=  extract_text(image, boxes)
    st.write(text)
