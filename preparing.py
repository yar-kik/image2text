import os
import json


class Preparing:
    def __init__(self, *, source: str = 'images/',
                 file_name: str = 'images_list.json'):
        self.source = source
        self.file_name = file_name

    def create_images_dir(self) -> None:
        """
        Create directory which will contain images
        :param source: name of directory
        :return: None
        """
        if not os.path.exists(self.source):
            os.mkdir(self.source)

    def create_file_with_images(self) -> None:
        """
        Create file and add images name
        :param source: source directory with images
        :param file_name: file with images name
        :return: None
        """
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump([], file)

    def start_preparing(self):
        self.create_images_dir()
        self.create_file_with_images()
