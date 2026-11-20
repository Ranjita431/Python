#add and update values
student = {
    "name": "Ranjita",
    "age": 21
}

student["grade"] = "A"

print(student)

#update
student["age"] = 22

print(student["age"])


#update multiple using update method
student = {"name": "Ranjita", "age": 21}

student.update({"age": 22, "course": "BEIT"})

print(student)