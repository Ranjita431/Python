#comprehensions
squares = []

for number in range(1, 6):
    squares.append(number ** 2)

print(squares)

squares = [number ** 2 for number in range(1, 6)]

print(squares)


#list comprehensions with conditions
numbers = [1, 2, 3, 4, 5]

doubles = [number * 2 for number in numbers]

print(doubles)