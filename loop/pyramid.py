for row in range(1,5):
    for col in range(row):
        print("*",end=" ")
    print()


for row in range(1,5):
    for col in range(1,row+1):
        print(col,end=" ")
    print()