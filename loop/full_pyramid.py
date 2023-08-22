for row in range(8):
    for col in range(8 -row):
        print(" ",end="")
    for k in range(2*row+1):
        print("*",end="")
    print()