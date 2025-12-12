info = {
    "name" : "Suru",
    "subjects" : ["python", "c", "Java"],
    "topics" : ("dict", "set"),
    "age" : 35,
    "is_adult" : True,   
 }

info["name"] = "Suraj"
info["surname"] = "Mochi"

print(info)

print(type(info))




# nested Dictionary
student = {
    "name" : "Suraj Chouhan",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

new_students = {"Bio" : "lodux"}
student.update(new_students)

print(student)

