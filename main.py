import pytesseract

from preparing import Preparing
from services import get_images_name, add_image_name, write_output_data, \
    get_all_images_name, get_text_from_image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
source = 'images/'
file_name = 'images_list.json'
preparing = Preparing(source=source, file_name=file_name)
preparing.start_preparing()
language = 'rus+eng'


for image_name in get_all_images_name():
    if image_name not in get_images_name():
        add_image_name(image_name)
        image_url = source + image_name
        text = get_text_from_image(image_url)
        write_output_data(text)
