from pytesseract import pytesseract

from services import ImageService, ProcessedImage
from argparse import ArgumentParser

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def main(args):
    image_service = ImageService(language=args.lang)
    all_images_in_source = ProcessedImage.get_all_images()
    for image_name in all_images_in_source:
        processed_images = ProcessedImage(image_name)
        image_service.start_processing(processed_images)


if __name__ == '__main__':
    parser = ArgumentParser(description="Program to convert image to text file")
    parser.add_argument('-l', '--lang',
                        help="Text language on a picture, for example 'rus', "
                             "'ukr' or 'eng'. It's also possible to combine "
                             "languages - 'rus+eng'. Default is 'rus'",
                        type=str, default='rus')
    parser.add_argument('image_folder', type=str)
    args = parser.parse_args()
    main(args)
