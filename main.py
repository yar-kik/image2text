from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
source = 'images/'
language = 'rus+eng'

with open('images_list.txt', 'r') as list_file:
    images_list = list_file.read()

for image_url in os.listdir(source):
    if image_url not in images_list:
        with open('images_list.txt', 'a') as list_file:
            list_file.write(image_url)
        image = Image.open(source + image_url)
        resized_image = image.resize(tuple(map(lambda x: 2 * x, image.size)))
        text = pytesseract.image_to_string(resized_image, lang=language)
        with open(f'output.txt', 'a', encoding='utf-8') as text_file:
            text_file.write(text)
