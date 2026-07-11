from typing import Optional

import jsonpickle
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"


# This class is not a dataclass since dataclasses are immutable and this class is later updated with the hint_bio
# instance attribute
class QuoteInformation:
    def __init__(self, quote_text: str, author: str, href: str):
        self.quote_text = quote_text
        self.author = author
        self.href = href
        self.hint_bio = ""


# Downloads the html one page at a time for quotes
def _download_quotes_html(page_number: int) -> (Optional[str], bool):
    response = requests.get(f"{BASE_URL}/page/{page_number}/")
    html = response.text

    if response.status_code != 200:
        print("ERROR!")
        print(
            f"URL: {BASE_URL}/page/{page_number}/ \nStatus Code: {response.status_code}"
        )
        return None, True
    if html.find("No quotes found!") > -1:
        return None, False
    else:
        return html, True


# Parses the html one page at a time for quotes and extracts the quote text, author, and href from each quote into a
# QuoteInformation object per quote which returns a list of QuoteInformation objects per page
def _parse_quotes_html(html: str) -> list[QuoteInformation]:
    soup = BeautifulSoup(html, "html.parser")

    quote_information = []
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        quote_text = (
            quote.find(class_="text").get_text().replace("“", "").replace("”", "")
        )
        author = quote.find(class_="author").get_text()
        href = quote.find("a").attrs["href"]
        quote_information.append(QuoteInformation(quote_text, author, href))
    return quote_information


# Downloads the html one page at a time for each href
def _download_bio_html(href: str) -> Optional[str]:
    response = requests.get(f"{BASE_URL}{href}")
    html = response.text

    if response.status_code != 200:
        print("ERROR!")
        print(f"URL: {BASE_URL}{href} \nStatus Code: {response.status_code}")
        return None
    else:
        return html


# Parses the html one page at a time for each href and extracts the author birthdate and the author birth location from
# each href into a concatenated string which returns the hint_bio string per page
def _parse_bio_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    href = soup.find_all(class_="author-details")
    for hint in href:
        author_birthdate = hint.find(class_="author-born-date").get_text()
        author_birth_location = hint.find(class_="author-born-location").get_text()
        hint_bio = f"{author_birthdate} {author_birth_location}"
        return hint_bio


# Retrieves quotes into a QuoteInformation object per quote which returns a list of QuoteInformation objects
def retrieve_quotes() -> list[QuoteInformation]:
    quotes = []
    for i in range(1, 101):
        html, should_continue = _download_quotes_html(i)

        if not should_continue:
            break
        if not html:
            continue

        parsed_quotes = _parse_quotes_html(html)
        for j in range(len(parsed_quotes)):
            bio_html = _download_bio_html(parsed_quotes[j].href)

            if not bio_html:
                continue

            parsed_hint_bio = _parse_bio_html(bio_html)
            parsed_quotes[j].hint_bio = parsed_hint_bio

        if parsed_quotes:
            quotes.extend(parsed_quotes)
    return quotes


def retrieve_quotes_and_pickle():
    quotes_data = retrieve_quotes()

    with open("../downloaded_data/data.json", "w") as file:
        pickle_quotes_data = jsonpickle.encode(quotes_data)
        file.write(pickle_quotes_data)


if __name__ == "__main__":
    retrieve_quotes_and_pickle()
