#Basic if
age = 20
if age >= 18:
    print('You are eligible to vote')


#Indentation in python
age = 20
if age >= 18:
    print("Adult") 

#if age >= 18:
#print("Adult") #This will give an error because the print statement is not indented properly

#if with a comparison
marks = 75

if marks >= 40:
    print("Pass")

#If and else 
marks = 30

if marks >= 40:
    print("Pass")
else:
    print("Fail")

#if elif and else
marks = 75

if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("Fail")

#Order matters in if elif else statements
marks = 85

if marks >= 40:
    print("Pass")
elif marks >= 80:
    print("A")  #output will be "Pass" because the first condition is true and the rest will not be checked