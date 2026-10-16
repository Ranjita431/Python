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

#removing items from a set
numbers = {10, 20, 30, 40}

numbers.remove(20)
numbers.discard(50)

print(numbers)

#to remove every item
numbers.clear()
print(numbers)

#checking whether an item is present in a set
fruits = {"apple", "banana", "mango"}

print("apple" in fruits)
print("orange" in fruits)
print("orange" not in fruits)


#set operations
python_students = {"Ram", "Sita", "Hari"}
java_students = {"Sita", "Hari", "Gita"}

#union
print(python_students | java_students)

#intersection
print(python_students & java_students)

#difference
print(python_students - java_students)

#symmetric difference
print(python_students ^ java_students)