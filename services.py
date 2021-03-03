import json
import os
from PIL import Image
import pytesseract

from preparing import Preparing


class ProcessedImage:
    """
    Class for image that will process
    """
    def __init__(self, source: str, image_name: str):
        self.source = source
        self.image_name = image_name
        if not os.path.exists(self.image_url):
            raise FileNotFoundError(f'"{self.image_name}"')

    def __str__(self) -> str:
        return self.image_name

    @property
    def image_url(self) -> str:
        """
        Get image url
        :return: image url
        """
        return self.source + self.image_name

    def get_resized_image(self) -> Image:
        """
        Make image bigger (up to 2 times)
        :return: image instance
        """
        image = Image.open(self.image_url)
        resized_image = image.resize(tuple(map(lambda x: 2 * x, image.size)))
        return resized_image


class DirectoryImage:
    """
    Class to manage image files (get, update, delete)
    """
    image_extensions = ['jpeg', 'png', 'jpg', 'gif', 'webp']
    file_name = "images_list.json"

    def __init__(self, source: str):
        self.source = source
        if not os.path.exists(source):
            raise FileNotFoundError(f'"{source}"')

    def get_processed_images(self) -> list:
        """
        Get processed images
        :return: list of processed images
        """
        with open(self.file_name, 'r') as list_file:
            images_list = json.load(list_file)
        return images_list

    def get_all_images(self) -> list:
        """
        Get all images in source directory
        :return: list with all images in source
        """
        files = [image for image in os.listdir(self.source)
                 if image.split('.')[-1].lower() in self.image_extensions]
        return files

    def add_processed_image(self, other: ProcessedImage) -> None:
        """
        Add processed image to list of processed images
        :return:
        """
        images_list = self.get_processed_images()
        images_list.append(other.image_name)
        with open(self.file_name, 'w') as list_file:
            json.dump(images_list, list_file)

    def delete_processed_images(self) -> None:
        """
        Delete processed images from source directory
        :return:
        """
        images_list = self.get_processed_images()
        for image in images_list:
            os.remove(self.source + image)
        print(f"Все изображения в папке '{self.source}' удалены")

    def clear_processed_images_file(self) -> None:
        """
        Clear file with already processed images
        :return: None
        """
        with open(self.file_name, 'w') as file:
            json.dump([], file)
        print("Названия обработаных изображений удалены")


class Service:
    """
    Class to make main function (get text from image)
    """
    def __init__(self, output_file: str, language: str, source: str):
        self.output_file = output_file
        if not output_file.endswith('.txt'):
            output_file += '.txt'
        self.language = language
        if not source.endswith('/'):
            source += '/'
        self.directory = DirectoryImage(source)
        self.all_images = self.directory.get_all_images()

    def write_output_data(self, text: str) -> None:
        """
        Write output data into file
        :param text: text from image
        :return: None
        """
        with open(self.output_file, 'a', encoding='utf-8') as text_file:
            text_file.write(text)

    def get_text_from_image(self, image: ProcessedImage) -> str:
        """
        Function to get text from image
        :param image: ProcessedImage instance
        :return: text from image
        """
        text = pytesseract.image_to_string(image.get_resized_image(),
                                           lang=self.language)
        return text

    def start_processing(self, image: ProcessedImage) -> None:
        """
        Start getting text from image
        :param image: ProcessedImage instance (image to get text)
        :return: None
        """
        if image.image_name not in self.directory.get_processed_images():
            self.directory.add_processed_image(image)
            text = self.get_text_from_image(image)
            self.write_output_data(text)
            print(f'Изображение "{image}" обработано!')

    def clear_output_file(self) -> None:
        """
        Clear output file
        :return: None
        """
        open(self.output_file, 'w').close()
        print(f"Файл '{self.output_file}' пуст")

    def start_cleaning(self) -> None:
        """
        Clean source directory with images (delete all images), clear
        output file
        :return: None
        """
        # self.delete_processed_images()
        # self.clear_processed_images_file()
        self.clear_output_file()
