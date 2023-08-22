emp={"id":100,"name":"hari","desig":"HR","salary":250000}
print(emp)

# print emp name
# print(emp["name"])


for key in emp:
    print(key,emp[key])


# Adding new key value pair
emp["gender"]="male"
print(emp)

# updating a value
# dictname["key"]=value

emp["salary"]=27000
print(emp["salary"])


# update employee salary withy current salary +2000

emp["salary"]+=2000
print(emp["salary"])

# check existence of a key
# key in dictionary

if("name" in emp):
    print("present")
else:
    print("not present")