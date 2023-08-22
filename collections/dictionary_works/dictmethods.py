students= { "roll":1234,"name":"hari","age":25,"course":"mca"}
print(students.values())


# values() will return vaalues
# keys() will return keys
# items will return both values andd keys


# for k,v in students.iitems():
#     print(k,v)


# get(key) fetching values wrt keys

# print students["names"])

print(students.get("names"))
print("file transfer")
print("database commit")

# pop(key)  remove item

students.pop("course")
print(students)

