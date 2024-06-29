favourite_book = input()

books_checked = 0

while True:
    current_book = input()

    if current_book == favourite_book:
        print(f'You checked {books_checked} books and found it.')
        break

    if current_book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {books_checked} books.')
        break

    books_checked += 1
