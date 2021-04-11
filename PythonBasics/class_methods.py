# class ClassTest:

#   # uses data inside the object

#     def instance_method(self):
#         print(f"Called instance_mthod of {self}")

# # used as factories

#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")


# # doesn't use the class for anything


#     @staticmethod
#     def static_method():
#         print("Called static_mthod.")


# test = ClassTest()
# test.instance_method()

# ClassTest.static_method()

# Class method example


class Book:
  # class property
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("Python 101", 600)
print(book)
print(book2)
