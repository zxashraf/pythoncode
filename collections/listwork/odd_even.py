numbers=[2,7,8,9,12,13]
odd=[]
even=[]
for i in numbers:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)