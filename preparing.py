import os
import json


class Preparing:
    source = 'images/'
    file_name = 'images_list.json'

    def __init__(self, output_file: str = 'output.txt'):
        self.output_file = output_file
        self.start_preparing()

    def create_images_dir(self) -> None:
        if not os.path.exists(self.source):
            os.mkdir(self.source)

    def create_file_for_images(self) -> None:
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump([], file)

    def start_preparing(self):
        self.create_images_dir()
        self.create_file_for_images()
