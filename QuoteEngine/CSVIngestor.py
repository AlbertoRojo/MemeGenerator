""" An Ingestor instance to read csv files. """

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """ Class that ingests info from csv. """
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0, sep = ',')

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], 
                                   row['author'])
            quotes.append(new_quote)

        return quotes