import unittest

from scraper import QuoteInformation, _parse_quotes_html, _parse_bio_html


class TestScraper(unittest.TestCase):
    def test__parse_quotes_html(self):
        with open("./test_data/test_page_1.html", "r") as file:
            page_1_html = file.read()
            self.got_quotes = _parse_quotes_html(page_1_html)
            self.expected_quotes = [
                QuoteInformation(
                    "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",
                    "Albert Einstein",
                    "/author/Albert-Einstein",
                ),
                QuoteInformation(
                    "It is our choices, Harry, that show what we truly are, far more than our abilities.",
                    "J.K. Rowling",
                    "/author/J-K-Rowling",
                ),
                QuoteInformation(
                    "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.",
                    "Albert Einstein",
                    "/author/Albert-Einstein",
                ),
                QuoteInformation(
                    "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.",
                    "Jane Austen",
                    "/author/Jane-Austen",
                ),
                QuoteInformation(
                    "Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.",
                    "Marilyn Monroe",
                    "/author/Marilyn-Monroe",
                ),
                QuoteInformation(
                    "Try not to become a man of success. Rather become a man of value.",
                    "Albert Einstein",
                    "/author/Albert-Einstein",
                ),
                QuoteInformation(
                    "It is better to be hated for what you are than to be loved for what you are not.",
                    "André Gide",
                    "/author/Andre-Gide",
                ),
                QuoteInformation(
                    "I have not failed. I've just found 10,000 ways that won't work.",
                    "Thomas A. Edison",
                    "/author/Thomas-A-Edison",
                ),
                QuoteInformation(
                    "A woman is like a tea bag; you never know how strong it is until it's in hot water.",
                    "Eleanor Roosevelt",
                    "/author/Eleanor-Roosevelt",
                ),
                QuoteInformation(
                    "A day without sunshine is like, you know, night.",
                    "Steve Martin",
                    "/author/Steve-Martin",
                ),
            ]

        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[0], self.expected_quotes[0])
        )
        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[1], self.expected_quotes[1])
        )
        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[2], self.expected_quotes[2])
        )
        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[3], self.expected_quotes[3])
        )
        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[4], self.expected_quotes[4])
        )
        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[5], self.expected_quotes[5])
        )
        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[6], self.expected_quotes[6])
        )
        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[7], self.expected_quotes[7])
        )
        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[8], self.expected_quotes[8])
        )
        self.assertTrue(
            self.compare_parsed_quote(self.got_quotes[9], self.expected_quotes[9])
        )

    def test__parse_bio_html(self):
        with open("./test_data/test_bio_page.html", "r") as file:
            bio_page_html = file.read()
            self.got_hint_bio = _parse_bio_html(bio_page_html)
            self.expected_hint_bio = "March 14, 1879 in Ulm, Germany"

        self.assertTrue(
            self.compare_parsed_hint_bio(self.got_hint_bio, self.expected_hint_bio)
        )

    @staticmethod
    def compare_parsed_quote(
        got_quote: QuoteInformation, expected_quote: QuoteInformation
    ) -> bool:
        return (
            got_quote.quote_text == expected_quote.quote_text
            and got_quote.author == expected_quote.author
            and got_quote.href == expected_quote.href
        )

    @staticmethod
    def compare_parsed_hint_bio(got_hint_bio: str, expected_hint_bio: str) -> bool:
        return got_hint_bio == expected_hint_bio


if __name__ == "__main__":
    unittest.main()
