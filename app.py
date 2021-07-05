import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except TypeError:
            print(f"Invalid extension")
            continue

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        for file_name in files:
            imgs.append(os.path.join(root, file_name))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    image_url = request.form.get("image_url")
    img_file = f"./static/{random.randint(0, 100000)}.jpg"
    quote = QuoteModel(request.form.get("author"),
                        request.form.get("body"))
    path = meme.make_meme(img_file, quote.body, quote.author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
