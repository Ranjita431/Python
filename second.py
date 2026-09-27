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
print(name.upper())

print(name.lower())