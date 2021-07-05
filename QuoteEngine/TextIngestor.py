
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open (path, "r") as myfile:
            data = myfile.read().splitlines()

            for row in data:
                body = row.split(' - ')[0]
                author = row.split(' - ')[1]
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes