import json
import os
from PIL import Image
import pytesseract

def get_images_name(file_name: str = 'images_list.json') -> list:
    """
    Get a list with images name
    :param source: source directory with images
    :param file_name:
    :return: list of images
    """
    with open(file_name, 'r') as list_file:
        images_list = json.load(list_file)
    return images_list


def get_all_images_name(source: str = 'images/') -> list:
    return os.listdir(source)


def add_image_name(image_name: str,
                   file_name: str = 'images_list.json') -> None:
    """
    Add new image new to file
    :param image_name:
    :param file_name:
    :return: None
    """
    images_list = get_images_name(file_name)
    images_list.append(image_name)
    with open(file_name, 'w') as list_file:
        json.dump(images_list, list_file)


def write_output_data(text: str, file_name: str = 'output.txt') -> None:
    """
    Function to write output data in file
    :param text:
    :param file_name:
    :return: None
    """
    with open(file_name, 'a', encoding='utf-8') as text_file:
        text_file.write(text)


def get_text_from_image(image_url: str, language: str = 'rus+eng') -> str:
    image = Image.open(image_url)
    resized_image = image.resize(tuple(map(lambda x: 2 * x, image.size)))
    text = pytesseract.image_to_string(resized_image, lang=language)
    return text
