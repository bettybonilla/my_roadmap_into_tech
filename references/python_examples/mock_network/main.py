from typing import Protocol, Optional

import requests


class Requester(Protocol):
    def get(self, url: str) -> Optional[str]:
        pass


class RealRequester:
    @staticmethod
    def get(url: str) -> Optional[str]:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        return None


class Parser:
    def __init__(self, requester: Requester):
        self.requester: Requester = requester

    def parse(self, url: str) -> str:
        response_text = self.requester.get(url)
        return response_text
