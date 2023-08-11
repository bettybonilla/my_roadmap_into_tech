"""
I've provided you with a dictionary called inventory:
inventory = {"croissant": 19, "bagel": 4, "muffin": 8, "cake": 1}
- Make a copy of inventory and save it to a variable called stock_list using a
dictionary method we've covered
- Add the value 18 to stock_list under the key "cookie"
- Remove “cake” from stock_list using a dictionary method we've covered
"""

# NO TOUCHING =================================================================
inventory = {"croissant": 19, "bagel": 4, "muffin": 8, "cake": 1}
# NO TOUCHING =================================================================

# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
print(stock_list)

# Add the value 18 to stock_list under the key "cookie"
stock_list["cookie"] = 18
print(stock_list)

# Remove "cake" from stock_list
stock_list.pop("cake")
print(stock_list)
