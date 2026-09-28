class Book:
    def __init__(self,book_id,title,author,category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True

    def display_books(self):
        status = "available" if self.available else "Issued"
        print("Book ID:",self.book_id)
        print("Title:",self.title)
        print("Author",self.author)
        print("Category:",self.category)
        print("status:",status)
    def issue_book(self):
        if self.available:
            self.available = False
            return True
        return False
    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False



class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
    def display_members(self):
        print("Member ID:",self.member_id)
        print("Member nama:",self.name)
        print("Member email:",self.email)
        print("Borrowed books")
        if len(self.borrowed_books)==0:
            print("No books borrowed")
        else:
            for book in self.borrowed_books:
                print(self.title)
    def borrow_book(self,book):
        self.borrowed_books.append(book)
    def return_book(self,book):
        if book in self.borrowed_book:
            self.borrowed_book.remove(book)
            return True
        return False



class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
        self.members = []
    def add_book(self,book):
        self.books.append(book)
        print("Book added successfully")
    def display_books(self):
        if len(self.books)==0:
            print("No books available")
            return
        for book in self.books:
            book.display_books()
    def search_book(self,keyword):
        found = False
        for book in self.books:
            if (keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()):
                book.display_book()
                found = True
        if not found:
            print("Book not found/available")
    def add_member(self,member):
        self.members.append(member)
        print("member added successfully")
    def display_members(self):
        if len(self.members)==0:
            print("No members available")
            return
        for member in self.members:
            member.display_members()
    def issue_book(self,book_id,member_id):
        book = None
        member = None
        for b in self.books:
            if b.book_id==book_id:
                book = b
                break
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if book is None:
            print("Book not Found")
            return
        if member is None:
            print("member not found")
            return
        if book.issue_book():
            member.borrow_book(book)
            print("book issued successfully")
        else:
            print("book is already issued")
    def return_book(self,book_id,member_id):
            book = None
            member = None
            for b in self.books:
                if b.book_id==book_id:
                    book = b
                    break
            for m in self.members:
                if m.member_id == member_id:
                    member = m
                    break
            if book is None:
                print("Book not Found")
                return
            if member is None:
                print("member not found")
                return
            if member.return_book(book):
                book.return_book(book)
                print("book returned successfully")
            else:
                print("this member has not borrowed this book")


library = Library("central Library")
book1 = Book(101,"Python","Guido","Programming")
book2 = Book(102,"Biography","APJ","Auto-biography")
library.add_book(book1)
library.add_book(book2)

member1 = Member(1,"Nandini","nandiniyannagiri@gmail.com")
library.add_member(member1)

print(library.display_books())
print(library.display_members())
