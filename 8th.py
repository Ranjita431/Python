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