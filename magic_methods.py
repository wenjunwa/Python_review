# Magic methods = Dunder methods (double underscores) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behavior of objects
from list_set_tuple import fruit_tuple


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author ==other.author

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, keyword):
        if keyword == "title":
            return self.title
        elif keyword =="author":
            return self.author
        else:
            return "None"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book4 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch, and the Wardrobe", "C.S Lewis", 172 )

print(book1)
print(book2 == book4)
print(book1 > book3)
print(book1 < book3)
print("Hobbit" in book2)
print(book1["Title"])

