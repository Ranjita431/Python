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


#convert strings to uppercase
names = ["ram", "sita", "hari"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)

#list of squares
squares = [x ** 2 for x in range(1, 6)]

print(squares)

#List comprehension with an if condition
numbers = [1, 2, 3, 4, 5, 6]
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)

#List comprehension with if-else
numbers = [1, 2, 3, 4, 5]

result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)

#Set comprehension
numbers = range(1, 11)

even_squares = {n ** 2 for n in numbers if n % 2 == 0}

print(even_squares)