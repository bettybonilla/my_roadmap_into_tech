from bs4 import BeautifulSoup

# Let's imagine this is the HTML we got back when we made a request to a website to get the HTML
# HTML will actually come back as a large multi-line string as shown below in the html variable
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special super-special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

# Then we can instantiate BeautifulSoup by saving it to a variable (soup) and use the BeautifulSoup() function and pass
# in the html variable containing the large HTML string as well as the "html.parser" string to specify we want to parse
# HTML since BeautifulSoup also supports parsing XML which is another markup language
soup = BeautifulSoup(html, "html.parser")
print(soup)
# This shows that BeautifulSoup parsed the HTML and it's no longer a large string now but an instance of BeautifulSoup
# which allows us to use methods on it - As mentioned the HTML is no longer a string
print(type(soup))

# ----------------------------------------------------------------------------------------------------------------------
# How to navigate between HTML elements relative to one another:
# Using tags:
# - .parent attribute - Returns the parent tag of a nested tag
# - .contents attribute - Returns a list of the nested contents in a tag
# - .next_sibling attribute - Returns the next tag on the same level of a tag
# - .previous_sibling attribute - Returns the previous tag on the same level of a tag
# Using searching methods:
# - .find_parent() method - Returns the parent tag of a nested tag (you can also pass in a specific parent tag)
# - .find_next_sibling() method - Returns the next tag on the same level of a tag while skipping newline characters (you
# can also pass in a specific attribute)
# - .find_previous_sibling() method - Returns the previous tag on the same level of a tag while skipping newline
# characters (you can also pass in a specific attribute)
# ----------------------------------------------------------------------------------------------------------------------

print("")
print("-------------------------------------------------------------------------------")
print("Using tags")
print("-------------------------------------------------------------------------------")
print("")

# Prints the HTML body tag - Each tag has been parsed into its own object
print(soup.body)
print("")

# Prints a list of the nested contents in the body tag
print(soup.body.contents)
print("")

# To print the first div tag in the body tag, you have to use index 1 since index 0 is the newline character
print(soup.body.contents[1])
print("")
# You can continue to chain the .contents attribute which descends into the next nested contents
print(soup.body.contents[1].contents)
print("")

# To print the next tag on the same level of a tag, you can use the .next_sibling attribute
# However, you have to chain it twice since the next sibling is a newline character
print(soup.body.contents[1].next_sibling.next_sibling)
print("")
# You can also navigate to this same tag by using its index with the .contents attribute
print(soup.body.contents[3])
print("")
# To print the previous tag on the same level of a tag, you can use the .previous_sibling attribute
# As mentioned, you have to chain it twice since the previous sibling is a newline character
print(soup.body.contents[3].previous_sibling.previous_sibling)
print("")

# Prints the parent tag of a nested tag
print(soup.find(class_="special").parent)
print("")
# You can continue to chain the .parent attribute which ascends into the next parent tag
print(soup.find(class_="special").parent.parent)

print("")
print("-------------------------------------------------------------------------------")
print("Using searching methods")
print("-------------------------------------------------------------------------------")
print("")

# To print the next tag on the same level of a tag, you can also use the .find_next_sibling() method
# This method does not require you to chain it twice since it skips newline characters until it actually finds the next
# tag unlike the .next_sibling attribute
print(soup.find(id="first").find_next_sibling())
# Prints newline character
# print(soup.find(id="first").next_sibling)
print("")
# To print the next tag on the same level of a tag while specifying an attribute, you can use the .find_next_sibling()
# method and pass in the specific attribute which skips tags that don't contain this attribute
# Skips <li>This list item is not special.</li>
print(soup.find(class_="special").find_next_sibling(class_="special"))
print("")
# As seen above with attributes, you can also chain methods
print(soup.find(id="first").find_next_sibling().find_next_sibling())
print("")
# You can also navigate to this same tag by using its index with the .contents attribute
print(soup.body.contents[5])
# Alternative code
# print(soup.find_all(attrs={"data-example": True})[1])
# print(soup.select("[data-example]")[1])
print("")
# To print the previous tag on the same level of a tag, you can also use the .find_previous_sibling() method
# This method also does not require you to chain it twice since it skips newline characters until it actually finds the
# previous tag unlike the .previous_sibling attribute
print(soup.select("[data-example]")[1].find_previous_sibling())
print("")
# To print the previous tag on the same level of a tag while specifying an attribute, you can also use the
# .find_previous_sibling() method and pass in the specific attribute which skips tags that don't contain this attribute
# Skips <li>This list item is not special.</li>
print(soup.find(class_="super-special").find_previous_sibling(class_="special"))
print("")

# Prints the parent tag of a nested tag
print(soup.find(class_="special").find_parent())
print("")
# You can also pass in a specific parent tag
print(soup.find(class_="special").find_parent("body"))
