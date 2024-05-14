# Quote Guessing Game

## Introduction

- In this project, you’ll be building a quote guessing game
    - When run, your program will scrape a website for a collection of quotes, pick one at random, and display it
    - The player will have four chances to guess who said the quote
    - After every wrong guess, they’ll get a hint about the person’s identity

## Specifications

1. Create a file which, when run, grabs data on every quote from the website: [https://quotes.toscrape.com/]()
2. You can use the `bs4` package and the `requests` package to get the data. For each quote you should grab the text of
   the quote, the name of the person who said the quote, and the href of the link to the person’s bio - Store all this
   information in a `list`.
3. Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
4. After each incorrect guess, the number of guesses remaining will decrement - If the player gets to zero guesses
   without identifying the person, the player loses and the game ends. If the player correctly identifies the person,
   the player wins!
5. After every incorrect guess, the player receives a hint about the person
    - For the first hint, make another request to the person’s bio page (this is why we originally scrape this data) and
      tell the player the person’s birthdate and birth location
    - The next two hints are up to you!
        - Some ideas to consider:
            - The first letter of the person’s first name
            - The first letter of the person’s last name
            - The number of letters in one of the names, etc.
6. When the game is over, ask the player if they want to play again - If yes, restart the game with a new quote. If no,
   the program is complete.
