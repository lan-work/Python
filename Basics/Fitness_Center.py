how_many_visitors = int(input())

how_many_are_training = 0
how_many_are_buying = 0
back_workouts = 0
chest_workouts = 0
legs_workouts = 0
abs_workouts = 0
protein_shakes = 0
protein_bars = 0

for i in range(how_many_visitors):
    visitor_does = input()

    if visitor_does == 'Back':
        back_workouts += 1
        how_many_are_training += 1
    elif visitor_does == 'Chest':
        chest_workouts += 1
        how_many_are_training += 1
    elif visitor_does == 'Legs':
        legs_workouts += 1
        how_many_are_training += 1
    elif visitor_does == 'Abs':
        abs_workouts += 1
        how_many_are_training += 1
    elif visitor_does == 'Protein shake':
        protein_shakes += 1
        how_many_are_buying += 1
    elif visitor_does == 'Protein bar':
        protein_bars += 1
        how_many_are_buying += 1

training_visitors_percentage = (how_many_are_training / how_many_visitors) * 100
buying_visitors_percentage = (how_many_are_buying / how_many_visitors) * 100

print(f'{back_workouts} - back')
print(f'{chest_workouts} - chest')
print(f'{legs_workouts} - legs')
print(f'{abs_workouts} - abs')
print(f'{protein_shakes} - protein shake')
print(f'{protein_bars} - protein bar')
print(f'{training_visitors_percentage:.2f}% - work out')
print(f'{buying_visitors_percentage:.2f}% - protein')
