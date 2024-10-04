# Bookstore Management System
books = [
    {"title": "Book A", "author": "Author A", "price": 300},
    {"title": "Book B", "author": "Author B", "price": 450},
    {"title": "Book C", "author": "Author C", "price": 150}
]

def add_book(title, author, price):
    books.append({"title": title, "author": author, "price": price})

def print_books():
    for book in books:
        print(book)

def check_book_by_title(title):
    for book in books:
        if book["title"] == title:
            return True
    return False

def remove_book(title):
    i = 0
    while i < len(books):
        if books[i]["title"] == title:
            del books[i]
        else:
            i += 1

def total_books():
    return len(books)

def total_value_of_books():
    total = 0
    for book in books:
        total += book["price"]
    return total

def most_expensive_book():
    return max(books, key=lambda book: book["price"])

def sort_books_by_price():
    return sorted(books, key=lambda book: book["price"])

def search_books_by_author(author):
    result = []
    for book in books:
        if book["author"] == author:
            result.append(book)
    return result

def filter_books_cheaper_than(price):
    result = []
    for book in books:
        if book["price"] < price:
            result.append(book)
    return result

def count_books_above_price(price):
    return len([book for book in books if book["price"] > price])

def authors_tuple():
    return tuple(book["author"] for book in books)

book_reviews = {}

def add_review(title, review):
    if title not in book_reviews:
        book_reviews[title] = []
    book_reviews[title].append(review)

def display_reviews(title):
    return book_reviews.get(title, [])

book_stock = {"Book A": 10, "Book B": 5, "Book C": 7}

def process_sale(title, quantity):
    if title in book_stock and book_stock[title] >= quantity:
        book_stock[title] -= quantity
        for book in books:
            if book["title"] == title:
                return book["price"] * quantity
    return "Not enough stock"

def check_stock_levels():
    for title in book_stock:
        print(f"{title}: {book_stock[title]} in stock")

def check_if_out_of_stock(title):
    return book_stock.get(title, 0) == 0

def book_titles_set():
    return set(book["title"] for book in books)

def merge_reviews(reviews1, reviews2):
    merged = reviews1.copy()
    for title, review in reviews2.items():
        if title in merged:
            merged[title] += review
        else:
            merged[title] = review
    return merged

def longest_book_title():
    longest = ""
    for book in books:
        if len(book["title"]) > len(longest):
            longest = book["title"]
    return longest

def replace_author(title, new_author):
    for book in books:
        if book["title"] == title:
            book["author"] = new_author

def find_books_with_word(word):
    result = []
    for book in books:
        if word in book["title"]:
            result.append(book)
    return result

def second_highest_priced_book():
    sorted_books = sorted(books, key=lambda book: book["price"], reverse=True)
    return sorted_books[1] if len(sorted_books) > 1 else None

def convert_titles_to_uppercase():
    for book in books:
        book["title"] = book["title"].upper()
