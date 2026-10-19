#dictionary
student = {
    "name": "Ranjita",
    "age": 21,
    "course": "BEIT"
}


print(student["name"])
print(student["age"])
print(student["course"])

print(student.get("grade"))
print(student.get("grade", "Not available"))

#add and update items in a dictionary
student = {
    "name": "Ranjita",
    "age": 21
}

student["grade"] = "A"

print(student)

#remove items
student = {
    "name": "Ranjita",
    "age": 21,
    "course": "BEIT"
}

student.pop("age")
print(student)

#using del
del student["course"]
print(student)

#Dictionary methods you should know
student = {
    "name": "Ranjita",
    "age": 21,
    "course": "BEIT"
}

print(student.keys())
print(student.values())
print(student.items())
print(len(student))

#Loop through keys
student = {"name": "Ranjita", "age": 21, "course": "BEIT"}

for key in student:
    print(key)

#loop through values
for value in student.values():
    print(value)

#use items
for key, value in student.items():
    print(key, ":", value)



#checking whether a key exists in a dictionary
student = {
    "name": "Ranjita",
    "age": 21
}

print("name" in student)
print("grade" in student)
print("grade" not in student)

#imporatnt in checks keys not values
print("Ranjita" in student)          # False
print("Ranjita" in student.values()) # True


#Bested dictionaries
students = {
    "student1": {
        "name": "Ranjita",
        "grade": "A"
    },
    "student2": {
        "name": "Sita",
        "grade": "B"
    }
}

print(students["student1"]["name"])
print(students["student2"]["grade"])

students["student1"]["name"]

#Dictionary keys: important rules
data = {
    "age": 20,
    "age": 22
}

print(data)