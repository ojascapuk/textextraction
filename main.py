# Load the uploaded image
img_4 = Image.open(image_path_4)

# Extract the text from the image using pytesseract
handwritten_text_4 = pytesseract.image_to_string(img_4)

# Output the extracted text
handwritten_text_4
