BASKET_PRICE = 1.50
WREATH_PRICE = 3.80
BUNNY_PRICE = 7.00

how_many_customers = int(input())
overall_money_spent = 0
overall_purchases_count = 0

for i in range(how_many_customers):
    purchases_count = 0
    money_spent = 0
    even_purchases = False

    while True:
        purchase_type = input()
        if purchase_type == 'Finish':
            break

        if purchase_type == 'basket':
            money_spent += BASKET_PRICE
        elif purchase_type == 'wreath':
            money_spent += WREATH_PRICE
        elif purchase_type == 'chocolate bunny':
            money_spent += BUNNY_PRICE

        purchases_count += 1

    if purchases_count % 2 == 0:
        money_spent -= (money_spent * 0.20)

    print(f'You purchased {purchases_count} items for {money_spent:.2f} leva.')

    overall_money_spent += money_spent
    overall_purchases_count += purchases_count

average_money_spent = overall_money_spent / how_many_customers

print(f'Average bill per client is: {average_money_spent:.2f} leva.')
