lst=[10,11,10,11,12,13]
i=0
while(i<len(lst)-1):
    if lst[i]==lst[i+1]:
        print(lst[i])
        i+=1
    else:
        i+=1