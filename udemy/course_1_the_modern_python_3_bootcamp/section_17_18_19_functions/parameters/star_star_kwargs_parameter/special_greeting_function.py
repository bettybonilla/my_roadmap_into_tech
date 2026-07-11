"""
Below is another example of how you can use **kwargs in a function to check for
specific input provided since, as mentioned, you're able to pass in as many
keyword arguments as you want with the **kwargs parameter
"""


# In the special_greeting() function below, the **kwargs parameter is used to
# check the key-value pairs in the kwargs dictionary which returns a string
# depending on the keyword arguments provided
def special_greeting(**kwargs: str) -> str:
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who you are..."


print(special_greeting(David="Hello"))
print(special_greeting(Bob="hello"))
print(special_greeting(David="special"))
print(special_greeting(Heather="hello", David="special"))
