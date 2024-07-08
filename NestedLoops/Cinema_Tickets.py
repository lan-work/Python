student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while True:
    movie_name = input()

    # КРАЙ НА ПРОГРАМАТА
    if movie_name == 'Finish':
        break

    free_seats = int(input())
    sold_tickets = 0
    occupancy = 0

    # -------------------------------------------------------------------------
    # ЗАПОЧВА ПРОДАЖБАТА НА БИЛЕТИ
    while free_seats > sold_tickets:
        ticket_type = input()

        # КРАЙ НА ПРОДАЖБАТА БИЛЕТИ
        if ticket_type == 'End':
            break

        sold_tickets += 1
        total_tickets += 1

        if ticket_type == 'student':
            student_tickets += 1
        if ticket_type == 'standard':
            standard_tickets += 1
        if ticket_type == 'kid':
            kid_tickets += 1

    # ИЗВЕЖДАНЕ НА РЕЗУЛТАТИ СЛЕД ВСЕКИ ФИЛМ
    occupancy = (sold_tickets / free_seats) * 100
    print(f'{movie_name} - {occupancy:.2f}% full.')
    # -------------------------------------------------------------------------

# ИЗВЕЖДАНЕ НА КРАЙНИТЕ РЕЗУЛТАТИ
print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.')
