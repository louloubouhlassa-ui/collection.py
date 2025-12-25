print ('===LIBRARY MANAGEMENT SYSTEM===')

#1- LIBRARY BOOK CATALOG

books = {
    "978-0134685991": {
        "title": "Effective Python",
        "author": "Brett Slatkin",
        "year": 2019,
        "copies": 3,
        "genre": "Programming"
    },
    "978-0135957059": {
        "title": "The Pragmatic Programmer",
        "author": "David Thomas",
        "year": 2019,
        "copies": 2,
        "genre": "Programming"
    },
    "978-0132350884": {
        "title": "Clean Code",
        "author": "Robert Martin",
        "year": 2008,
        "copies": 4,
        "genre": "Programming"
    }
}
#2- LIBRARY MEMBERS
members = {
    "M001": {
        "name": "Alice Johnson",
        "email": "alice@university.edu",
        "type": "Student",
        "join_date": (2024, 9, 1)
    },
    "M002": {
        "name": "Bob Smith",
        "email": "bob@university.edu",
        "type": "Faculty",
        "join_date": (2024, 9, 1)
    },
    "M003": {
        "name": "Carol White",
        "email": "carol@university.edu",
        "type": "Student",
        "join_date": (2024, 10, 15)
    }
}

#3- BORROWED BOOKS TRACKING
borrowed_books ={"M001": ["978-0134685991", "978-0135957059"],
    "M002": ["978-0132350884"],
    "M003": ["978-0134685991"]
}


# 4. Book Genres 
genres = {"Programming", "Fiction", "Science", "History", "Mathematics", "Art"}


# 5. Weekly Library Hours 

library_hours = {
    "Monday": "9:00 AM - 8:00 PM",
    "Tuesday": "9:00 AM - 8:00 PM",
    "Wednesday": "9:00 AM - 8:00 PM",
    "Thursday": "9:00 AM - 8:00 PM",
    "Friday": "9:00 AM - 6:00 PM",
    "Saturday": "10:00 AM - 4:00 PM",
    "Sunday": "Closed"
}


# 6. Popular Books Tracking

popular_books = [
    ("978-0134685991", 45),
    ("978-0132350884", 38),
    ("978-0135957059", 32)
]


# 7. Reserved Books 

reserved_books = {
    "978-0134685991",
    "978-0135957059",
    "978-0132350884"
}


# DISPLAY INFORMATION

print("\n--- All Books ---")
for isbn, info in books.items():
    print(f"\nISBN: {isbn}")
    print(f"Title: {info['title']}")
    print(f"Author: {info['author']}")
    print(f"Year: {info['year']}")
    print(f"Copies: {info['copies']}")
    print(f"Genre: {info['genre']}")

print("\n--- All Members ---")
for member_id, info in members.items():
    print(f"\nMember ID: {member_id}")
    print(f"Name: {info['name']}")
    print(f"Email: {info['email']}")
    print(f"Type: {info['type']}")
    print(f"Join Date: {info['join_date']}")

print("\n--- Library Hours ---")
for day, hours in library_hours.items():
    print(f"{day}: {hours}")

print("\n--- Available Genres ---")
for genre in genres:
    print(genre)


# OPERATIONS

# Find book by ISBN
isbn_search = "978-0134685991"
print("\n--- Book Search by ISBN ---")
if isbn_search in books:
    print(books[isbn_search])

# Find member by ID
member_search = "M001"
print("\n--- Member Search by ID ---")
if member_search in members:
    print(members[member_search])

# Books borrowed by a member
print("\n--- Books Borrowed by Member M001 ---")
for isbn in borrowed_books["M001"]:
    print(isbn)

# Add a new genre
genres.add("Philosophy")

# Check if ISBN is reserved
print("\n--- Reserved Book Check ---")
print("978-0134685991" in reserved_books)

# Top 3 most popular books
print("\n--- Top 3 Popular Books ---")
for isbn, count in popular_books:
    print(f"{isbn} - {count} times")

# ADVANCED OPERATIONS

# Members who borrowed a specific book
print("\n--- Members who borrowed 'Effective Python' ---")
for member_id, isbns in borrowed_books.items():
    if "978-0134685991" in isbns:
        print(members[member_id]["name"], f"({member_id})")

# Total copies available
total_copies = 0
for book in books.values():
    total_copies += book["copies"]

print("\nTotal number of copies available:", total_copies)

# Union of borrowed and reserved ISBNs
all_borrowed = set()
for isbns in borrowed_books.values():
    all_borrowed.update(isbns)

union_isbns = all_borrowed | reserved_books
print("\n--- Borrowed OR Reserved ISBNs ---")
print(union_isbns)

# Intersection of borrowed and reserved ISBNs
intersection_isbns = all_borrowed & reserved_books
print("\n--- Borrowed AND Reserved ISBNs ---")
print(intersection_isbns)