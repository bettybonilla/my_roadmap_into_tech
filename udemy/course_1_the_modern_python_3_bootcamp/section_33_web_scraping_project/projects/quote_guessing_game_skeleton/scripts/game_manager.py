import random
from typing import List

from scripts.scraper import QuoteInformation


class GameManager:
    def __init__(self, quotes: List[QuoteInformation]):
        random.shuffle(quotes)
        self.quotes = quotes
        self.retry_count = 0
