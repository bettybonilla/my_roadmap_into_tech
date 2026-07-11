from typing import Optional


class QuoteInformation:
    def __init__(self, quote: str, author: str):
        self.quote = quote
        self.author = author
        self.hint = ""
        self.href = ""


def _download_quote_html(page_number) -> (Optional[str], bool):
    # todo if html.find("No quotes found!") == -1 return None
    return None, True


def _download_bio_html(href) -> str:
    pass


def _parse_quotes_html(markup: str) -> list[QuoteInformation]:
    pass


def _parse_bio_hint(markup: str) -> str:
    # todo parse the hint from the markup
    return ""


def retrieve_quotes() -> list[QuoteInformation]:
    quotes: List[QuoteInformation] = []
    for i in range(1, 101):
        html, should_continue = _download_quote_html(i)
        
        if not should_continue:
            break

        if not html:
            continue


        parsed_quotes = _parse_quotes_html(html)
        for j in range(len(parsed_quotes)):
            bio_html = _download_bio_html(parsed_quotes[j].href)
            if not bio_html:
                continue

            parsed_quotes[j].hint = _parse_bio_hint(bio_html)

        if parsed_quotes:
            quotes.extend(parsed_quotes)
    # todo save data (quotes) to file
    return quotes
