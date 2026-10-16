#create a set
fruits = {"apple", "banana", "mango"}

print(fruits)
print(type(fruits))

#empty set
empty_set = {}
print(type(empty_set))

empty_set = set()

print(type(empty_set))


#sets do not support indexing
#fruits = {"apple", "banana", "mango"}

#print(fruits[0])

#we can do 
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)

#adding items to a set
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)

#update
numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)