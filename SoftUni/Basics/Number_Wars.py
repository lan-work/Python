player1_name = input()
player2_name = input()

player1_score = 0
player2_score = 0

number_wars = False

while True:
    player1_card = input()
    if player1_card == 'End of game':
        print(f'{player1_name} has {player1_score} points')
        print(f'{player2_name} has {player2_score} points')
        break

    player1_card = int(player1_card)
    player2_card = int(input())

    diff = abs(player1_card - player2_card)

    if player1_card > player2_card:
        if number_wars:
            print(f'{player1_name} is winner with {player1_score} points')
            break
        player1_score += diff

    elif player2_card > player1_card:
        if number_wars:
            print(f'{player2_name} is winner with {player2_score} points')
            break
        player2_score += diff
    else:
        if number_wars:
            break
        number_wars = True
        print('Number wars!')
        continue
