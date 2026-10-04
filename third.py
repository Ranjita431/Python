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

if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("Fail")

#Taking user input 
#age = int(input("Enter your age: "))

#if age >= 18:
 #   print("You can vote.")
#else:
 #   print("You cannot vote.")

#Multiple conditions with and 
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")

#OR 
is_student = False
has_discount_card = True

if is_student or has_discount_card:
    print("Discount available")
else:
    print("No discount")

#NOT
is_student = False
has_discount_card = True

if is_student or has_discount_card:
    print("Discount available")
else:
    print("No discount")