students={"rollno":1,"name":"Ashraf","marks":100}

if("marks" in students):
    print("marks","is present")
else:
    print("marks","not present")

# print all values

for key in students:
    print(key,students[key])

# add a new key value pair

students["class"]=5
print(students)


# add 50rs discount 

students["marks"]-=50
print(students)

