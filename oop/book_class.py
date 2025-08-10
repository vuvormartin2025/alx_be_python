# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: user-friendly format."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: used for debugging and recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"