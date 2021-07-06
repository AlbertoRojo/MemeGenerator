""" An engine to create the image of the meme"""

from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:
    """ Class to create the image. """
    def __init__(self, out_path):
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=None) -> str:
        """Create a new meme With a Text Greeting

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the quote to be inserted in the meme.
            author {str} -- The author of the quote
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        try:
            img = Image.open(img_path)
        except:
            print("Error loading the image")
        # resize img to desired width
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        # add a quote in the meme img
        message = f'"{text}" - {author}'
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('arial.ttf', size=20)
        draw.text((10, 30), message, font=font) # , fill='white'
        out_path = f"{self.out_path}/{random.randint(0, 100000)}.jpeg"

        img.save(out_path)
        return out_path