import argparse
import os

from scripts.game_manager import GameManager
from scripts.scraper import retrieve_quotes

SAVED_DATA_LOCATION = "data.pickle"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='QuoteGame',
        description='Guess a quote')
    parser.add_argument('-d', '--download_quotes', action='store_true', help='Download quotes from the web')
    args = parser.parse_args()

    if args.download_quotes:
        print('Downloading quotes...')
        _ = retrieve_quotes()

    quotes = []
    # check if file of quotes exists
    check_file = os.path.isfile(SAVED_DATA_LOCATION)
    if check_file:
        # TODO unpickle into Quotes
        quotes = []
        pass
    else:
        quotes = retrieve_quotes()

    manager = GameManager(quotes)

    # application logic
