"""
The below shows how you can use **kwargs in a function
"""


# The fav_colors() function below prints the 3 arguments provided which each
# correspond and are assigned directly to an individual parameter
def fav_colors(Colt: str, Ruby: str, Ethel: str) -> str:
    print(Colt)
    print(Ruby)
    print(Ethel)


fav_colors(Colt="purple", Ruby="red", Ethel="teal")


# However, we can use **kwargs as a parameter to provide as many keyword
# arguments as we want instead of having separate parameters for each keyword
# argument like the 3 originally provided above which corresponded and were
# assigned directly to each individual parameter
def fav_colors(**kwargs: str) -> str:
    # Just like with the *args parameter, we only need the ** star star
    # operator in the parameter but outside of the parameter we don't need the
    # ** star star operator as shown below in the print() function
    # This prints the kwargs provided in the function call as a dictionary
    print(kwargs)

    # Since our kwargs is a dictionary, we need to iterate through the
    # dictionary in order to get the kwargs and print them
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")

    # We can also use person, color as the item variables in the for loop
    # for person, color in kwargs.items():
    #     print(f"{person}'s favorite color is {color}")


# As mentioned, now we can pass in as many keyword arguments as we want since
# we are using **kwargs as a parameter
fav_colors(Colt="purple", Ruby="red", Ethel="teal")
fav_colors(Colt="purple", Ruby="red", Ethel="teal", Ted="blue")
fav_colors(Colt="royal deep amazing purple")


# The below shows that the parameter doesn't have to be named **kwargs, it can
# be named anything you want as long as it starts with the ** star star
# operator
def fav_colors(**people: str) -> str:
    print(people)

    for person, color in people.items():
        print(f"{person}'s favorite color is {color}")


fav_colors(Colt="royal deep amazing purple")
