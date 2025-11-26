# lib/author_book_contract.py

class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Book title must be a string")
        self.title = title
        Book.all.append(self)


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return a list of contracts associated with this author"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of books associated with this author via contracts"""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create a new contract with a book, date, and royalties"""
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")
        return Contract(author=self, book=book, date=date, royalties=royalties)

    def total_royalties(self):
        """Return the total royalties from all contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that have the same date"""
        return [contract for contract in cls.all if contract.date == date]
