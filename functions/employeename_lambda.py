# create a function for returning employee name
employee={"id":100,"name":"vijay","department":"hr","salary":250000}


# def get_name(emp):
#     return emp.get("name")
# print(get_name(employee))

#  create a lambda function for returning employee salary

# get_salary=lambda emp:emp.get("salary")
# print(get_salary(employee))



# *args positional argument takes any numbers of parameter type tuple

# def addition(*args):
#     return sum(args)

# print(addition(10,20))
# print(addition(10,20,30))


Addition=lambda *args:sum(args)
print(Addition(10,20,30))

max_nums=lambda *args:max(args)
print(max_nums(10,2,3,4,90))