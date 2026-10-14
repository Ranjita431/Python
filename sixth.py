#Creating a tuple
# List
fruits = ["apple", "banana", "mango"]

# Tuple
fruits = ("apple", "banana", "mango")

student = ("Ranjita", 3.50, "BEIT", 5)

print(student)

#accessing tuple elements
student = ("Ranjita", 3.50, "BEIT", 5)

print(student[0])
print(student[1])
print(student[-1])

#tuple slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[::-1])

#Immutable tuple
fruits = ("apple", "banana", "mango")

fruits[0] = "orange"