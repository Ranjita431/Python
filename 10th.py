#Comprehension of a list
squares = []

for number in range(1, 6):
    squares.append(number ** 2)

print(squares)


for number in range(5,10):
    squares.append(number ** 2)

print(squares)


#List comprehension
numbers = [2, 3, 4, 5, 6]
squares = [numbers ** 2 for numbers in numbers]
print(squares)


#Convert strings to uppercase
names = ["ram", "sita", "hair"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)