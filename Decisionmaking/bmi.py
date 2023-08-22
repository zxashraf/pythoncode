weight=80
height=2
bmi=weight/(height)**2
print(bmi)
if(bmi<=18.5):
    print("under weight")
elif(bmi<=24.9):
    print("normal weight")
elif(bmi<=29.9):
    print("over weight")
elif(bmi <34.4):
    print("obesity level 1")
elif (bmi<39.9):
    print("obesity level 2")
else:
    print("obesity level 3")