import pytesseract

from preparing import Preparing
from services import get_processed_images, add_new_image, write_output_data, \
    get_all_images_in_source, get_text_from_image

source = 'images/'
file_name = 'images_list.json'
preparing = Preparing(source=source, file_name=file_name)
preparing.start_preparing()
language = 'rus+eng'


for image_name in get_all_images_in_source():
    if image_name not in get_processed_images():
        add_new_image(image_name)
        image_url = source + image_name
        text = get_text_from_image(image_url)
        write_output_data(text)
