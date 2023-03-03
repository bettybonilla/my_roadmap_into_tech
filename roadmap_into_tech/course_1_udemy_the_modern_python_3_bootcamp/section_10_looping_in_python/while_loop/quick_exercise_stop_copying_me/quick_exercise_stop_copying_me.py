"""
Repeat everything until the user says "stop copying me"
"""

sister = print("Hey, how's it going?")
brother = input().lower()

while brother != "stop copying me":
    sister = brother
    print(sister)
    brother = input().lower()
print("UGH FINE YOU WIN 🙄")
