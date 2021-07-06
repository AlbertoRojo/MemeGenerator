""" Base interface for ingestor. """

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """ Class to identify an ingestible file"""
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass