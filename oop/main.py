from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)             # _str_
    print(repr(my_book))       # _repr_
    del my_book                # _del_

if __name__ == "__main__":
    main()