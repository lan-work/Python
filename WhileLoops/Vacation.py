money_needed = float(input())
money_available = float(input())

money_saved = money_available
days_counter = 0
consecutive_spend_days = 0

while money_saved < money_needed:
    days_counter += 1
    spend_or_save = input()
    daily_amount = float(input())

    if spend_or_save == 'save':
        money_saved += daily_amount
        consecutive_spend_days = 0

    elif spend_or_save == 'spend':
        consecutive_spend_days += 1
        if consecutive_spend_days >= 5:
            print(f'You can\'t save the money.')
            print(days_counter)
            break

        if daily_amount > money_saved:
            money_saved = 0
        else:
            money_saved -= daily_amount
else:
    print(f'You saved the money for {days_counter} days.')
