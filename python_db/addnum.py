num=int(input("enter number"))
try:
    num=int(num)
    print(num**3)
except Exception as e:
    raise Exception("operand must be number")