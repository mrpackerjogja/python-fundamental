"""
Program Perulangan membaca buku dengan while
"""

book_counted = 4
print(f'amount of book are: {book_counted}')
print('Momo said, "Read all your book"')

amount_of_book_has_readed = 0
while amount_of_book_has_readed < book_counted:
    amount_of_book_has_readed = amount_of_book_has_readed + 1
    print(f'book {amount_of_book_has_readed} has readed')

print(f'amount of book has readed is {amount_of_book_has_readed}')

