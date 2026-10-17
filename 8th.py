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