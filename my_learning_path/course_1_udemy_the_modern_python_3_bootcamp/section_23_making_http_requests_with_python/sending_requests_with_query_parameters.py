"""
References
- https://icanhazdadjoke.com/api
"""

from pprint import pprint

import requests

BASE_URL = "https://icanhazdadjoke.com/search"

response = requests.get(
    BASE_URL,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1},
)
data = response.json()


if __name__ == "__main__":
    print(type(data))
    print(data)
    print(data["results"])
    print(f"status: {data['status']}")
    print("")

    pprint(data)
    print("")
    pprint(data["results"])
