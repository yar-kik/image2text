from services import ImageService, ProcessedImage

language = 'ukr'
image_service = ImageService(language=language)
image_service.start_preparing()
all_images_in_source = ProcessedImage.get_all_images()

for image_name in all_images_in_source:
    processed_images = ProcessedImage(image_name)
    image_service.start_processing(processed_images)
