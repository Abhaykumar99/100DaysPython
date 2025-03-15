# ============================================================
# Day 74: Library Management System (Final OOPs Exercise)
# ============================================================
# Combines: Classes, Inheritance, Encapsulation, File I/O, JSON
# ============================================================

import json
import os
from datetime import date, timedelta

class Book:
    def __init__(self, isbn, title, author, year, copies=1):
        self.isbn   = isbn
        self.title  = title
        self.author = author
        self.year   = year
        self.total_copies     = copies
        self.available_copies = copies

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, d):
        b = cls(d['isbn'], d['title'], d['author'], d['year'], d['total_copies'])
        b.available_copies = d['available_copies']
        return b

    def __str__(self):
        return f"[{self.isbn}] '{self.title}' by {self.author} ({self.year}) — {self.available_copies}/{self.total_copies} available"


class Member:
    def __init__(self, member_id, name, email):
        self.member_id    = member_id
        self.name         = name
        self.email        = email
        self.borrowed     = []   # List of {isbn, due_date}

    def to_dict(self):
        return {"member_id": self.member_id, "name": self.name,
                "email": self.email, "borrowed": self.borrowed}

    @classmethod
    def from_dict(cls, d):
        m = cls(d['member_id'], d['name'], d['email'])
        m.borrowed = d.get('borrowed', [])
        return m


class Library:
    DATA_FILE = "library_data.json"

    def __init__(self, name):
        self.name    = name
        self.books   = {}    # isbn → Book
        self.members = {}    # member_id → Member
        self._load()

    def add_book(self, book):
        self.books[book.isbn] = book
        print(f"✅ Added: {book}")
        self._save()

    def register_member(self, member):
        self.members[member.member_id] = member
        print(f"✅ Registered: {member.name}")
        self._save()

    def borrow_book(self, member_id, isbn, days=14):
        member = self.members.get(member_id)
        book   = self.books.get(isbn)

        if not member:
            return "❌ Member not found."
        if not book:
            return "❌ Book not found."
        if book.available_copies < 1:
            return f"❌ No copies of '{book.title}' available."

        due_date = (date.today() + timedelta(days=days)).isoformat()
        book.available_copies -= 1
        member.borrowed.append({"isbn": isbn, "title": book.title, "due": due_date})
        self._save()
        return f"✅ {member.name} borrowed '{book.title}'. Due: {due_date}"

    def return_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book   = self.books.get(isbn)

        if not member or not book:
            return "❌ Member or book not found."

        borrowed_titles = [b['isbn'] for b in member.borrowed]
        if isbn not in borrowed_titles:
            return f"❌ {member.name} hasn't borrowed '{book.title}'."

        member.borrowed = [b for b in member.borrowed if b['isbn'] != isbn]
        book.available_copies += 1
        self._save()
        return f"✅ '{book.title}' returned by {member.name}."

    def search(self, query):
        query = query.lower()
        found = [b for b in self.books.values()
                 if query in b.title.lower() or query in b.author.lower()]
        if found:
            for b in found: print(f"  {b}")
        else:
            print("  No matching books found.")

    def list_all_books(self):
        print(f"\n📚 {self.name} — All Books:")
        for book in self.books.values():
            print(f"  {book}")

    def _save(self):
        data = {
            "books":   {isbn: b.to_dict() for isbn, b in self.books.items()},
            "members": {mid: m.to_dict() for mid, m in self.members.items()},
        }
        with open(self.DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def _load(self):
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE) as f:
                data = json.load(f)
            self.books   = {isbn: Book.from_dict(b) for isbn, b in data.get('books',{}).items()}
            self.members = {mid: Member.from_dict(m) for mid, m in data.get('members',{}).items()}


# --- DEMO ---
if __name__ == "__main__":
    lib = Library("City Public Library")

    lib.add_book(Book("978-0-7432-7356-5", "The Alchemist",          "Paulo Coelho",    1988))
    lib.add_book(Book("978-0-06-112008-4", "To Kill a Mockingbird",  "Harper Lee",      1960, 2))
    lib.add_book(Book("978-0-7432-7357-2", "1984",                   "George Orwell",   1949, 3))

    lib.register_member(Member("M001", "Alice",   "alice@example.com"))
    lib.register_member(Member("M002", "Bob",     "bob@example.com"))

    lib.list_all_books()

    print(lib.borrow_book("M001", "978-0-7432-7356-5"))
    print(lib.borrow_book("M002", "978-0-7432-7356-5"))  # No copies!

    print(lib.return_book("M001", "978-0-7432-7356-5"))

    print("\nSearch 'orwell':")
    lib.search("orwell")

    # Cleanup
    if os.path.exists("library_data.json"):
        os.remove("library_data.json")
