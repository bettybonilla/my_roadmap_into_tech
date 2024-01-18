def say_sup():
    return f"Sup! My __name__ is {__name__}"


# This code will only run if the file is the main file
if __name__ == "__main__":
    print(say_sup())
