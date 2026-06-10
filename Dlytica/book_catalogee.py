class Book:
    total_books = 0

    def __init__(self, title, author, genre, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

        Book.total_books += 1

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["title"],
            data["author"],
            data["genre"]
        )
    @classmethod
    def get_total(cls):
        return f"Total books registered: {cls.total_books}"

    def borrow(self):

        if self.available == False:
            raise ValueError(f"{self.title} is already borrowed")

        self.available = False


    def return_book(self):

        if self.available == True:
            raise ValueError(f"{self.title} is not borrowed")

        self.available = True


    def __str__(self):

        status = "✓" if self.available else "✗"

        return f"[{status}] {self.title} | {self.author} | {self.genre}"



b1 = Book("Python Crash Course", "Eric Matthes", "Programming")

b2 = Book("Sapiens", "Yuval Noah Harari", "History")


b3 = Book.from_dict({
    "title": "Deep Work",
    "author": "Cal Newport",
    "genre": "Productivity"
})


b4 = Book("Clean Code", "Robert Martin", "Programming")


b1.borrow()
b2.borrow()


print(b1)
print(b2)
print(b3)
print(b4)


b1.return_book()

print(b1)


try:
    b2.borrow()

except ValueError as e:
    print(e)


print(Book.get_total())