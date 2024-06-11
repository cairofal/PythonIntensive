for value in range(1,5):
    print(value)

#Precisa de correção
list(range(1,10))
print(range)


even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)


digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#Exemplo de list compreheension
squares = [value**2 for value in range(1,11)]
print(squares)

#Copiando uma lista
my_foods = ['pizza', 'healthy food', 'beans']

my_friends_foods = my_foods[:]
print(my_friends_foods) 

my_friends_foods.append('Lasanha')