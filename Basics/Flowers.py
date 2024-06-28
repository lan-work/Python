import math

MAGNOLIAS_PRICE = 3.25
HYACINTHS_PRICE = 4
ROSES_PRICE = 3.50
CACTI_PRICE = 8
TAX_PERCENTAGE = 0.05

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_cost = float(input())

turnover = (magnolias * MAGNOLIAS_PRICE + hyacinths * HYACINTHS_PRICE + roses * ROSES_PRICE + cacti * CACTI_PRICE)
tax = turnover * TAX_PERCENTAGE
profit = turnover - tax
diff = abs(profit - gift_cost)

if profit >= gift_cost:
    print(f'She is left with {int(math.floor(diff))} leva.')
else:
    print(f'She will have to borrow {int(math.ceil(diff))} leva.')
