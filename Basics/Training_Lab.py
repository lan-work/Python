width_m = float(input())
height_m = float(input())

DOOR = 1
CATHEDRA = 2
CORRIDOR_WIDTH_CM = 100

WORKPLACE_WIDTH_CM = 120
WORKPLACE_HEIGHT_CM = 70

width_cm = width_m * 100
height_cm = height_m * 100

workplaces_columns = (height_cm - CORRIDOR_WIDTH_CM) // 70
workplaces_rows = width_cm // 120

workplaces_total = workplaces_columns * workplaces_rows - DOOR - CATHEDRA

print(int(workplaces_total))
