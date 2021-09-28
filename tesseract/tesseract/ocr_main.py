import click
import logging
import pytesseract
import numpy as np
from PIL import Image
from logging import getLogger

logger = getLogger('pylog')
logger.setLevel(logging.DEBUG)
file_handler = None

@click.command()
@click.option('--input', type=click.STRING, help='Input file path.')
@click.option('--output', type=click.STRING, help='Output file path.')
@click.option('--verbose', type=click.STRING, help='Log file path')

def do_ocr(input, output, verbose):
    img = np.array(Image.open(input))
    text = pytesseract.image_to_string(img)
    __write_to_file(text, output)
    __start_file_log(verbose)


def __write_to_file(text, output):
    f = open(output, "w")
    f.write(text)
    f.close()

def __start_file_log(filename):
    global file_handler
    file_handler = logging.FileHandler(filename, "w")
    logger.addHandler(file_handler)

if __name__ == '__main__':
    do_ocr()
