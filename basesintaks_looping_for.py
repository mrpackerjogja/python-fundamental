"""
Program Perulangan membaca buku dengan for
"""

book_counted = 4
print(f'amount of book are: {book_counted}')
print('Momo said, "Read all your book"')

amount_of_book_has_readed = 0
for amount_of_book_has_readed in range(1, book_counted + 1):
    print(f'book {amount_of_book_has_readed} has readed')

print(f'amount of book has readed is {amount_of_book_has_readed}')
