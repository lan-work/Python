GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

GASOLINE_DISCOUNT = 0.18
DIESEL_DISCOUNT = 0.12
GAS_DISCOUNT = 0.08

gasoline_club_price = GASOLINE_PRICE - GASOLINE_DISCOUNT
diesel_club_price = DIESEL_PRICE - DIESEL_DISCOUNT
gas_club_price = GAS_PRICE - GAS_DISCOUNT

fuel_type = input()
fuel_loaded = float(input())
club_card = input()

discount_percentage = 0.00
total_cost = 0

if fuel_loaded > 25:
    discount_percentage = 0.10
elif fuel_loaded >= 20:
    discount_percentage = 0.08

have_discount = True if discount_percentage != 0.00 else False
have_club_card = True if (club_card == 'Yes') else False

if fuel_type == 'Gasoline':
    total_cost = (fuel_loaded * gasoline_club_price) if have_club_card else (fuel_loaded * GASOLINE_PRICE)

elif fuel_type == 'Diesel':
    total_cost = (fuel_loaded * diesel_club_price) if have_club_card else (fuel_loaded * DIESEL_PRICE)

elif fuel_type == 'Gas':
    total_cost = (fuel_loaded * gas_club_price) if have_club_card else (fuel_loaded * GAS_PRICE)

if have_discount:
    total_cost -= (total_cost * discount_percentage)

print(f'{total_cost:.2f} lv.')
