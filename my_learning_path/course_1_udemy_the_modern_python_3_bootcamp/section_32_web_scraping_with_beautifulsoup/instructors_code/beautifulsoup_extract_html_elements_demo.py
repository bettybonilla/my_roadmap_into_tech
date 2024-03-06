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
    <li class="special super-special">This list item is also special.</li>
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
print("")

# ----------------------------------------------------------------------------------------------------------------------
# How to extract data in HTML elements:
# - .get_text() method - Extracts the inner text of an element
# - .name attribute - Extracts the tag name of an element
# - .attrs attribute - Extracts a dictionary of attributes with their key-value pairs
# - You can also extract attribute values using square brackets [] with their attribute key
# ----------------------------------------------------------------------------------------------------------------------

print(soup.select(".special"))
element = soup.select(".special")[0]
print(element)
# Extracts the inner text from the first special class
print(element.get_text())
print("")

# Uses a for loop to extract all the inner text from the special classes
for i in soup.select(".special"):
    print(i.get_text())
print("")

# Extracts the tag name from the first special class
print(element.name)
print("")

# Uses a for loop to extract all the tag names from the special classes
for i in soup.select(".special"):
    print(i.name)
print("")

# Extracts a dictionary of attributes from the first special class
print(element.attrs)
print("")

# Uses a for loop to extract all the dictionary of attributes from the special classes
# Elements can have more than one class which are separated by a space in the HTML element and are printed in a list
for i in soup.select(".special"):
    print(i.attrs)
print("")

# Extracts the attribute value using square brackets [] with the attribute key from the first special class
print(element.attrs["class"])
print("")

# Uses a for loop to extract all attribute values using square brackets [] with their attribute key from the special
# classes
for i in soup.select(".special"):
    print(i.attrs["class"])
print("")

# Another way to extract an attribute value is to use square brackets [] with the attribute key directly on an HTML tag
# using the .find() method
print(soup.find("li")["class"])
print(soup.find("h3")["data-example"])
print(soup.find("div")["id"])
print("")

# You can also call the .attrs attribute directly on an HTML tag using the .find() method to extract a dictionary of
# attributes
print(soup.find("li").attrs)
print(soup.find("h3").attrs)
print(soup.find("div").attrs)
