#Loop
#for i in range(100):
#    print("Hello")

#For loop with break
#for number in [1, 2, 3, 4, 5]:
#    print(number)

#Range
#for number in range(5):
#    print(number)

#range(start, stop)
#for number in range(1, 6):
#    print(number)

#range(start, stop, step)
#for number in range(1, 11, 2):
#    print(number)

#Counting backwards
#for number in range(5, 0, -1):
#    print(number)

# Looping through a string
name = "Ranjita"

for character in name:
    print(character)

# Looping through a string with an index
name = "Ranjita"

for i in range(len(name)):
    print(i, name[i])


#enumerate() function
name = "Ranjita"

for index, character in enumerate(name):
    print(index, character)

#for loop with conditions
for number in range(1, 11):
    if number % 2 == 0:
        print(number)


#Printing with odd number
for number in range(1, 11):
    if number % 2 == 0:
        print(number)

#while loop
for number in range(1, 11):
    if number % 2 != 0:
        print(number)


#example
number = 1

while number <= 5:
    print(number)
    number += 1


#infinite loop
#number = 1

#while number <= 5:
#    print(number)

#break
for number in range(1, 11):
    if number == 5:
        break

    print(number)

#continue
for number in range(1, 11):
    if number == 5:
        break

    print(number)