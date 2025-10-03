from pprint import pprint

import requests

BASE_URL = "https://icanhazdadjoke.com"

response = requests.get(BASE_URL, headers={"Accept": "application/json"})
data = response.json()

if __name__ == "__main__":
    print(type(data))
    print(data)
    print(data["joke"])
    print(f"status: {data['status']}")
    print("")

    # The built-in pprint module can be used to prettify a dictionary to make it more readable in terminal :-)
    pprint(data)
