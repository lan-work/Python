print("//----- Default end='\\n'-----//")
print(1)
print(2)
print(3)
print(1, 2, 3, end='!')
print('\n\n')

print('//----- Duplicate Placeholders -----//')
print('{1} + {1} * {1} = {0}'.format(3 + 3 * 3, 3))
print('\n\n')

print('//----- 2 ** 10 -----//')
print(2 ** 10)
print('\n\n')

# В Python не можем директно да конкатенираме число към даден текст
print('//----- Concatenation -----//')
a = 5.5
b = 3.4
result = 'The sum is: ' + str(int(a + b))
print(result)
