VIP_TICKET_PRICE = 499.99
NORMAL_TICKET_PRICE = 249.99

budget = float(input())
cathegory = input()
group = int(input())

# ИЗЧИСЛЯВАНЕ НА РАЗХОДИТЕ ЗА ТРАНСПОРТ
transportation_cost = 0.00

if group >= 50:
    transportation_cost = budget * 0.25
elif group >= 25:
    transportation_cost = budget * 0.40
elif group >= 10:
    transportation_cost = budget * 0.50
elif group >= 5:
    transportation_cost = budget * 0.60
else:
    transportation_cost = budget * 0.75

# СТОЙНОСТ НА БИЛЕТИТЕ
tickets_total_cost = (group * VIP_TICKET_PRICE) if cathegory == 'VIP' else (group * NORMAL_TICKET_PRICE)
final_cost = tickets_total_cost + transportation_cost

diff = abs(final_cost - budget)

if budget >= final_cost:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
