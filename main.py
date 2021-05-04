from pytesseract import pytesseract

from services import ProcessedImage, Service
from argparse import ArgumentParser

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def main(args):
    image_service = Service(language=args.lang, output_file=args.output_file,
                            source=args.image_folder)
    all_images_in_source = image_service.all_images
    if args.clear:
        image_service.start_cleaning()
        return
    if args.delete:
        image_service.directory.delete_processed_images()
        return
    for image_name in all_images_in_source:
        processed_images = ProcessedImage(args.image_folder, image_name)
        image_service.start_processing(processed_images)


if __name__ == '__main__':
    parser = ArgumentParser(description="Program to convert image to text file")
    parser.add_argument('-l', '--lang',
                        help="Text language on a picture, for example 'rus', "
                             "'ukr' or 'eng'. It's also possible to combine "
                             "languages - 'rus+eng'. Default is 'rus'",
                        type=str, default='rus')
    parser.add_argument('-c', '--clear', action='store_const', const=True)
    parser.add_argument('-d', '--delete', action='store_const', const=True)
    parser.add_argument('--image_folder', type=str, default='images/')
    parser.add_argument('--output_file', type=str, default='output_file.txt')
    args = parser.parse_args()
    main(args)
