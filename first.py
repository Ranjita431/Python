print("Hello, World")
#print("A")
#print("B")
#print("C")

name = "Ranjita"
#print(name)
#print(Name)  this can't be run because python is case sensitive and Name is not defined.

print("My name is " + name)
print("I am learning python programming")

age = 20
gpa = 3.90
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

x = 10
print(x)
print(type(x))

x = "Hello"
print(x)
print(type(x))

Name = "Ram"
print(Name)
NAME = "Ramesh"
print(NAME)

age , gps , address = 90 , 4.00 , "Balkumari"  #we can assign multiple values to multiple variables in a single line.
print(age)
print(gps)
print(address)

# Operators in python
a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)


num = 20
print(num % 2 == 0)

#Comparision operators

y = 10

print(y == 10)
print(y != 10)
print(y > 5)
print(y < 5)
print(y >= 10)
print(y <= 10)

#Logical operators
age = 30
print(age > 18 and age < 45)

age1 = 22
print(age1 >=23 and age1 <= 22)

#True AND True = True
#True AND False = False
#False AND True = False
#False AND False = False

age2 = 30
#print( age2 > 18 or age2 < 2)
#print( age2 > 33 or age2 < 28)  if one of the condition is true then the output will be true.

#NOT

#is_student = True
#print(not is_student)  #if the value is true then it will return false and vice versa.

is_student = False
print(not is_student)  #if the value is true then it will return false and vice versa.


#Assignment operators
x = 10
#x += 5 #x = x + 5
#x -= 6 #x = x - 6
#x *= 6 #x = x * 6
#x /= 6 #x = x / 6
#x %= 6 #x = x % 6
#x //= 6 #x = x // 6
x **= 6 #x = x ** 6
print(x)


#Identity Operators here is and is not are identity operators which are used to compare the objects, not the values. It checks whether the two objects are the same or not.
a = 10
print(a is 10)

b = 20
print(b is not 20)

c = 30
print( c is not 30)


#Membership Operators
#in and not in are membership operators which are used to test whether a sequence is presented in an object or not. It returns True if the value is found in the sequence and False if the value is not found in the sequence.

name = 'Ranjita Thapa Chhetri'
print('p' in name)
print('I' in name)
print('i' in name)


number = 27
if(number % 2 == 0):
    print("The number is even")
else:
    print("The number is Odd")

#Strings in python
name = "Ranjita"
college = 'NCIT'   #They both are same, we can use single or double quotes to define a string in python.


age = "20" #This is string because it is in quotes. If we remove the quotes then it will be an integer.
age = 20

#we can check the type of variable using type() function.

#String Indexing
name = 'Ranjita Thapa Chhteri'
print(name[12])
print(name[3])

#Negative Indexing
name = "Ramesh"
print(name[-1])
print(name[3])
print(name[-3])

