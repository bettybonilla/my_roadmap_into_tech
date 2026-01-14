# Example code for accessing all query arguments from client without needing to define all of them as query parameters


from fastapi import FastAPI
from fastapi import Request

app = FastAPI()


@app.get("/")
async def read_item(r: Request) -> dict[str, str]:
    print(r.query_params)
    print("--------------")
    print(r.query_params.keys())
    print("--------------")
    print(r.query_params.values())
    print("--------------")
    print(r.query_params.items())
    print("--------------")
    print(r.query_params.get("shiba"))
    print("--------------")
    # just returning random data to ensure the client is hitting the server
    return {"foo": "bar"}


# ----------------------------------------


# curl command to interact with the above server code:
# curl 'localhost:8000/?skip=0&name=marc&hello=world&shiba=hachi'
# NOTE: curl commands with query parameters must be passed as a string since both the ? character and the & character
# already exist as key characters and will otherwise raise the zsh: no matches found error
