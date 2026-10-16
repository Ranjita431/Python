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