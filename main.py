from pytesseract import pytesseract

from services import ImageService, ProcessedImage

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

language = 'rus+eng'
image_service = ImageService(language=language)
all_images_in_source = ProcessedImage.get_all_images()

for image_name in all_images_in_source:
    processed_images = ProcessedImage(image_name)
    image_service.start_processing(processed_images)

