from unittest import TestCase

from main import Requester


class TestParser(TestCase):
    def test_parse(self):
        from main import Parser

        class MockRequester(Requester):
            def get(self, url: str) -> str:
                if url == 'http://example.com':
                    return '<html><div>foobar</div><html>'
                return None

        mock_requester = MockRequester()
        parser = Parser(mock_requester)
        self.assertEqual(parser.parse('http://example.com'), '<html><div>foobar</div><html>')
