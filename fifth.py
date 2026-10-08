#creating a list 
names = ["Ranjita", "Alex", "John"]
marks = [80, 75, 92, 68]
student = ["Ranjita", 21, 3.50, True]

print(names[0])
print(names[2])

#negative indexing
print(names[-1])
print(names[-2])

#list slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#mutable list
names = ["Ranjita", "Alex", "John"]

names[1] = "David"

print(names)

#len() function
names = ["Ranjita", "Alex", "John"]

print(len(names))

#.append() method
names = ["Ranjita", "Alex"]

names.append("John")

print(names)


#.insert() method
names = ["Ranjita", "Alex"]

names.append("John")

print(names)


#.extend()
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)

print(a)

#remove() method
names = ["Ranjita", "Alex", "John"]

names.remove("Alex")

print(names)


#.pop() method
names = ["Ranjita", "Alex", "John"]

removed = names.pop(1)

print(removed)
print(names)

#del
names = ["Ranjita", "Alex", "John"]

del names[1]

print(names)

#.clear() method
names = ["Ranjita", "Alex", "John"]

names.clear()

print(names)

#checking if an item exists in a list
names = ["Ranjita", "Alex", "John"]

print("Ranjita" in names)
print("David" in names)

#Looping through a
names = ["Ranjita", "Alex", "John"]

for name in names:
    print(name)


#list + if
marks = [35, 67, 82, 45, 91]

for mark in marks:
    if mark >= 40:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

#finding the largst number in a list
numbers = [10, 25, 7, 42, 18]

print(max(numbers))
print(min(numbers))
print(min(numbers))