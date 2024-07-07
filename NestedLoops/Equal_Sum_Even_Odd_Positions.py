start = int(input())
end = int(input())

for i in range(start, end + 1):
    # ----------- BREAKS THE NUMBER AND SUMS ODDS AND EVENS -------------- START
    current_number = i
    position = 1
    sum_odds = 0
    sum_evens = 0

    while current_number > 0:
        # LOGIC
        remainder = current_number % 10

        if position % 2 == 0:
            sum_odds += remainder
        else:
            sum_evens += remainder

        position += 1

        # UPDATE WHILE CONDITION
        current_number //= 10
    # ----------- BREAKS THE NUMBER AND SUMS ODDS AND EVENS -------------- END

    if sum_odds == sum_evens:
        print(i, end=' ')
