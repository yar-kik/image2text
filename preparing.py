import os
import json


class Preparing:

    def __init__(self, file_name: str = 'images_list.json'):
        self.file_name = file_name
        self.start_preparing()

    def create_file_for_images(self) -> None:
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump([], file)

    def start_preparing(self):
        self.create_file_for_images()
