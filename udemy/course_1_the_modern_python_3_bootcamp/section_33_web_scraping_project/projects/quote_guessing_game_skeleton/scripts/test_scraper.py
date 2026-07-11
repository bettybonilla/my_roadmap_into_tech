from unittest import TestCase

from scripts import scraper


class Test(TestCase):
    def test_parse_quotes_html(self):
        with open("/Users/marcsantiago/Desktop/skeleton/scripts/test_data/test_markup.html", "r") as file:
            data = file.read()
            got = scraper._parse_quotes_html(data)

        # TODO: Add the other 9 quotes from page 1
        want = [
            scraper.QuoteInformation(
                quote="“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
                author="Albert Einstein"),

        ]
        self.assertEquals(want, got)
