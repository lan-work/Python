breads_to_be_made = int(input())

highest_score = 0
best_baker = ''
is_winning = False

for i in range(breads_to_be_made):

    baker_name = input()
    bread_total_score = 0
    is_winning = False

    while True:
        stop_or_score = input()
        if stop_or_score == 'Stop':
            break

        score = int(stop_or_score)
        bread_total_score += score

    # РЕЗУЛТАТИ ЗА ТЕКУЩИЯ КОЗУНАК
    print(f'{baker_name} has {bread_total_score} points.')

    if bread_total_score > highest_score:
        is_winning = True
        highest_score = bread_total_score
        best_baker = baker_name

    if is_winning:
        print(f'{baker_name} is the new number 1!')

print(f'{best_baker} won competition with {highest_score} points!')
