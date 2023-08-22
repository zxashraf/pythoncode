lst=[1,3,4,8,9]
element=9
flag=0
for i in range(0,len(lst)):
    if(element==lst[i]):
        print(element,"is found")
        flag=1
        break
if(flag==0):
        print(element,"is not found")
        
        
    