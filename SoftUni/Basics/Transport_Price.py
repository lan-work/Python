BUSS_TARIFF = 0.09
TRIAN_TARIFF = 0.06
TAXI_DAY_TARIFF = 0.79
TAXI_NIGHT_TARIFF = 0.90
TAXI_INITIAL_FEE = 0.70

distance_km = int(input())
night_or_day = input()

total_cost = 0.00

if distance_km >= 100:
    total_cost = distance_km * TRIAN_TARIFF
elif distance_km >= 20:
    total_cost = distance_km * BUSS_TARIFF
else:
    if night_or_day == 'day':
        total_cost = TAXI_INITIAL_FEE + (distance_km * TAXI_DAY_TARIFF)
    else:
        total_cost = TAXI_INITIAL_FEE + (distance_km * TAXI_NIGHT_TARIFF)

print(f'{total_cost:.2f}')