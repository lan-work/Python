FUEL_NEEDED = 25

fuel_type = input()
fuel_available = float(input())
if fuel_type == 'Diesel' or fuel_type == 'Gasoline' or fuel_type == 'Gas':
    if fuel_available >= FUEL_NEEDED:
        print(f'You have enough {fuel_type.lower()}.')
    else:
        print(f'Fill your tank with {fuel_type.lower()}!')
else:
    print(f'Invalid fuel!')
