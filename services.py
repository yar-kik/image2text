import json
import os
from PIL import Image
import pytesseract

from preparing import Preparing


class ProcessedImage(Preparing):
    image_extensions = ['jpeg', 'png', 'jpg', 'gif', 'webp']

    def __init__(self, image_name):
        self.image_name = image_name
        if not os.path.exists(self.image_url):
            raise FileNotFoundError(f'"{self.image_name}"')

    def __str__(self):
        return self.image_name

    @property
    def image_url(self) -> str:
        return self.source + self.image_name

    @classmethod
    def get_processed_images(cls) -> list:
        with open(cls.file_name, 'r') as list_file:
            images_list = json.load(list_file)
        return images_list

    @classmethod
    def get_all_images(cls) -> list:
        files = [image for image in os.listdir(cls.source)
                 if image.split('.')[-1] in cls.image_extensions]
        return files

    def add_processed_image(self) -> None:
        images_list = self.get_processed_images()
        images_list.append(self.image_name)
        with open(self.file_name, 'w') as list_file:
            json.dump(images_list, list_file)

    def get_resized_image(self):
        image = Image.open(self.image_url)
        resized_image = image.resize(tuple(map(lambda x: 2 * x, image.size)))
        return resized_image


class ImageService(Preparing):
    pytesseract.pytesseract.tesseract_cmd = \
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def __init__(self, output_file: str = 'output.txt',
                 language: str = 'rus+eng'):
        self.output_file = output_file
        self.language = language

    def write_output_data(self, text: str) -> None:
        with open(self.output_file, 'a', encoding='utf-8') as text_file:
            text_file.write(text)

    def get_text_from_image(self, image: ProcessedImage) -> str:
        text = pytesseract.image_to_string(image.get_resized_image(),
                                           lang=self.language)
        return text

    def start_processing(self, image: ProcessedImage) -> None:
        if image.image_name not in image.get_processed_images():
            image.add_processed_image()
            text = self.get_text_from_image(image)
            self.write_output_data(text)
            print(f'Изображение "{image}" обработано!')
