"""
- This is a bit different - Every character has an ASCII code (basically, a
number that represents it) and Python has a function called chr() that will
return a string if you provide the corresponding integer ASCII code in the
chr() function
    - Ex:
        chr(65) will return 'A'
        chr(66) will return 'B'
        All the way up to:
        chr(90) will return 'Z'
- Your task is to create a dictionary that maps ASCII keys to their
corresponding letters
    - Use a dictionary comprehension and the chr() function and save the
    result to the answer variable
    - You only need to care about capital letters (65-90)
    - The end result will look like this:
    1. {
    2.     65: 'A',
    3.     66: 'B',
    4.     67: 'C',
    5.     68: 'D',
    6.     69: 'E',
    7.     70: 'F',
    8.     71: 'G',
    9.     72: 'H',
    10.     73: 'I',
    11.     74: 'J',
    12.     75: 'K',
    13.     76: 'L',
    14.     77: 'M',
    15.     78: 'N',
    16.     79: 'O',
    17.     80: 'P',
    18.     81: 'Q',
    19.     82: 'R',
    20.     83: 'S',
    21.     84: 'T',
    22.     85: 'U',
    23.     86: 'V',
    24.     87: 'W',
    25.     88: 'X',
    26.     89: 'Y',
    27.     90: 'Z'
    28. }
"""

answer = {count: chr(count) for count in range(65, 91)}
print(answer)
