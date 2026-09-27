#String slicing
name = 'Ranjita '
print(name[0:4])
print(name[0:3])
#Leaving start or end empty
print(name[:3])
print(name[3:])
#Slicing with step
print(name[0:6:2])

#Reverse a string
print(name[::-1])

#String length
name = 'Ranjita Thapa Chhetri'
print(len(name))

clz = 'Nepal College of Information Technology'
print(len(clz))

#Joining two strings

first_name = 'Ranjita Thapa'
second_name = 'Chhetri'

Total_name = first_name + ' ' + second_name
print(Total_name)


#printing a string multiple times    
print('Ranjita ' *10)

print('*'*20 + 'Hello World' + '*'*20)


#Important string methods
name = 'Ranjita Thapa Chhetri'
print(name.upper()) #turns all the letters of the string into upper case

print(name.lower()) # truns all the letters of the string into lower case

print(name.title()) #makes the first letter of each word capital

print(name.capitalize()) #make only the first letter of the string capital


#Strip 
name ='         Rajesh Thapa Chhteri      '
print (name.strip()) #remove all the space from the start and end of the string


#.replace() method

text ='Im going to be millionaire before 2030'
print(text.replace('millionaire', ' trillianore'))


#.find() method
text ='Im going to be millionaire before 2030'
print(text.find('millionaire')) #returns the index of the first occurrence of the substring. If not found, it returns -1.


#usind in operator to check if a substring is present in the string
text = 'I love programming in python'
print('Programmming' in text)
print('programming' in text)