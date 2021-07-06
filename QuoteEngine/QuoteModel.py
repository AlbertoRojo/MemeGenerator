""" File to create a quote input"""


class QuoteModel():
    """ Creates a quote class """
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'"{self.body}" - {self.author}'