"""
The below shows the diamond problem in multiple inheritance
"""


# The diamond problem can occur when you are using multiple inheritance since
# it can be very confusing and hard to follow in a large code base along with
# polymorphism and method overriding - As mentioned, this is why multiple
# inheritance and polymorphism should be used with caution for this reason
class A:
    def method(self):
        print("This method is in class A")


class B(A):
    def method(self):
        print("This method is in class B")


class C(A):
    def method(self):
        print("This method is in class C")


class D(B, C):
    pass


d = D()
d.method()
