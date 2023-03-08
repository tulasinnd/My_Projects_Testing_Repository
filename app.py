import cv2
import pytesseract
import numpy as np

# Load image
img = cv2.imread('image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to remove noise
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours and draw bounding boxes around text blocks
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w > 50 and h > 50:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the new image with bounding boxes around text blocks
cv2.imshow('Image with Text Blocks', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
