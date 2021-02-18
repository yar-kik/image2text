import json
import os
from PIL import Image
import pytesseract

from preparing import Preparing


class ImageService(Preparing):
    def __init__(self, output_file: str = 'output.txt',
                 language: str = 'rus+eng'):
        super().__init__()
        self.output_file = output_file
        self.language = language
        pytesseract.pytesseract.tesseract_cmd = \
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def get_processed_images(self) -> list:
        with open(self.file_name, 'r') as list_file:
            images_list = json.load(list_file)
        return images_list

    def get_all_images_in_source(self) -> list:
        return os.listdir(self.source)

    def add_processed_image(self, image_name: str) -> None:
        images_list = self.get_processed_images()
        images_list.append(image_name)
        with open(self.file_name, 'w') as list_file:
            json.dump(images_list, list_file)

    def write_output_data(self, text: str) -> None:
        with open(self.file_name, 'a', encoding='utf-8') as text_file:
            text_file.write(text)

    def get_text_from_image(self, image_url: str) -> str:
        image = Image.open(image_url)
        resized_image = image.resize(tuple(map(lambda x: 2 * x, image.size)))
        text = pytesseract.image_to_string(resized_image, lang=self.language)
        return text
