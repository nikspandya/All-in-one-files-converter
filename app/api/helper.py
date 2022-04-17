import uuid
from pdf2image import convert_from_path
from PIL import Image


def conversion_logic(file_for_conversion, output_file_format):
    """
    takes the input file & target file extensions
    convert files to target file format
    all pages of pdf file converted to multiple images
    all images should converted to RGB type before saving to avoid image channels conflict
    """
    if file_for_conversion.lower().endswith(('.jpg', '.png', '.bmp', '.ppm', '.gif', '.tiff')):
        Image.open(file_for_conversion).convert('RGB').save(file_for_conversion.split('.')[0] + '_' +
                                                            str(uuid.uuid4()) + str(output_file_format.lower()))

    elif file_for_conversion.lower().endswith(('.pdf')):
        images_ppm = convert_from_path(file_for_conversion)
        for i, img in enumerate(images_ppm):
            img.convert('RGB').save(file_for_conversion.split('.')[0] + '_page_' + str(i) + '_' + str(uuid.uuid4()) +
                                    str(output_file_format.lower()))
