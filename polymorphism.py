# operator Overloading is valid in Python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        total = self.pages + other.pages
        return Book(total)

    def __str__(self):
        return str(self.pages)


b1 = Book(200)
b2 = Book(100)
b3 = Book(300)
print(b1 + b2 + b3)


# Method overloading
class Test:
    def sum(self, *a):
        total = 0
        for x in a:
            total = total + x
            print("The sum is:", total)


t = Test()
t.sum(10)
t.sum(10, 10)


# method overriding

class P:
    @staticmethod
    def property():
        print("Land|Cash|gold|Power")

    @staticmethod
    def marriage():

        print("X|Y|Z")


class C(P):
    @staticmethod
    def marriage():

        print("A|B|C")


c = C()
c.property()
c.marriage()