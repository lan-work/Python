num_sectors = ord(input())
num_rows = int(input())
initial_seats = int(input())

sectors_start = ord('A')

total_seats = 0

for sector in range(sectors_start, num_sectors + 1):
    rows_start = 1

    for row in range(1, num_rows + 1):
        num_seats = initial_seats if row % 2 != 0 else initial_seats + 2

        for seat in range(97, 97 + num_seats):
            total_seats += 1
            print(f'{chr(sector)}{row}{chr(seat)}')

    num_rows += 1

print(total_seats)
