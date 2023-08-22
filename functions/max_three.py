def max_three(n1,n2,n3):
    if(n1>n2) and (n1>n3):
        return n1
    elif(n2>n3):
        return n2
    else:
        return n3
print(max_three(1,2,3)) 

def max_three(n1,n2,n3):
    return n1 if (n1>n2) and (n1>n3) else n2 if n2>n3 else n3
print(max_three(1,2,3))
