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
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
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
# Once parsed, there are several ways to navigate the HTML:
# Using tags:
# - .find() method - Returns first matching tag
# - .find_all() method - Returns a list of all matching tags
# Using CSS selectors:
# - .select() method - Returns a list of elements matching a CSS selector
# - CSS selectors:
# - select by id: "#foo"
# - select by class: ".bar"
# - select children: div > p
# - select descendants: div p
# ----------------------------------------------------------------------------------------------------------------------

print("")
print("-------------------------------------------------------------------------------")
print("Using tags")
print("-------------------------------------------------------------------------------")
print("")

# Prints the HTML body tag - Each tag has been parsed into its own object
print(soup.body)
print("")

# Prints only the first div tag in the body tag
print(soup.body.div)
print("")
# Alternative code using the .find() method
print(soup.body.find("div"))
print("")

# As mentioned, this shows that each tag has been parsed into its own object (div tag is not a string)
d = soup.find("div")
print(type(d))
print("")

# Prints a list of all the div tags in the body tag
print(soup.body.find_all("div"))
print("")
# Prints a list of all the div tags in the HTML not just in the body tag
print(soup.find_all("div"))
print("")

# You can also specify id and class attributes and other attributes
# Since an id can only be used once to an HTML tag, you would use the .find() method
print(soup.find(id="first"))
print("")
# Since a class can be used to group several HTML tags, you would use the .find_all() method
# You have to use class_ instead of class since this is already a reserved thing in Python and will raise a SyntaxError
# Prints the special classes in a list
print(soup.find_all(class_="special"))
print("")
# To specify other attributes, you would use the attrs keyword argument with the .find_all() method
# Prints the data-example attributes in a list
print(soup.find_all(attrs={"data-example": True}))

print("")
print("-------------------------------------------------------------------------------")
print("Using CSS selectors")
print("-------------------------------------------------------------------------------")
print("")

# As mentioned above, the .select() method returns a list of elements matching a CSS selector
# Prints the first element with an id of "first" in a list
# Alternative code to using print(soup.find(id="first"))
print(soup.select("#first"))
print("")
# To access the object itself while using the .select() method, use its index which takes it out of the list
print(soup.select("#first")[0])
print("")
# Prints the special classes in a list
# Alternative code to using print(soup.find_all(class_="special"))
print(soup.select(".special"))
print("")
# Prints the data-example attributes in a list
# Alternative code to using print(soup.find_all(attrs={"data-example": True}))
print(soup.select("[data-example]"))
