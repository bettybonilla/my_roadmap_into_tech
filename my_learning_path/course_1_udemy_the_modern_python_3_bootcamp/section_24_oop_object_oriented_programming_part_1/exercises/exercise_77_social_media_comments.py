"""
It's time to actually define your own class!
- Suppose we're creating a social network application where users can comment
on posts and photos
- Create a class called Comment
    - Each comment should have the following attributes:
        - username - The username of the person who created the comment (like
        "bluethecat")
        - text - The actual comment itself (like "omg so cute!" or "hahah")
        - likes - The number of likes the comment has (it should default to 0)
    - The following code should work:
        c = Comment("davey123", "lol you're so silly", 3)
        c.username  # "davey123"
        c.text  # "lol you're so silly"
        c.likes  # 3
        another_comment = Comment("rosa77", "soooo cute!!!")
        another_comment.username  # "rosa77"
        another_comment.text  # "soooo cute!!!"
        another_comment.likes  # 0
    - Hint: The __init__ dunder method is like any other function. To add a
    default value to a parameter, just use the = assignment operator and
    remember that your default parameters need to go towards the end!
"""


class Comment:
    def __init__(self, username: str, text: str, likes: int = 0):
        self.username = username
        self.text = text
        self.likes = likes


c = Comment("davey123", "lol you're so silly", 3)
print(c.username)
print(c.text)
print(c.likes)

another_comment = Comment("rosa77", "soooo cute!!!")
print(another_comment.username)
print(another_comment.text)
print(another_comment.likes)
