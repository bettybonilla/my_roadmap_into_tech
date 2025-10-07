import requests
from pydantic import BaseModel

BASE_URL = "https://icanhazdadjoke.com/search"


class Result(BaseModel):
    id: str
    joke: str


class DadJoke(BaseModel):
    current_page: int
    limit: int
    next_page: int
    previous_page: int
    results: list[Result]
    search_term: str
    status: int
    total_jokes: int
    total_pages: int


if __name__ == "__main__":
    response = requests.get(
        BASE_URL, headers={"Accept": "application/json"}, params={"term": "cat"}
    )
    dad_joke = DadJoke(**response.json())
    print(dad_joke)
    print("")

    # More appropriate than the built-in pprint module
    print(dad_joke.model_dump_json(indent=4))
