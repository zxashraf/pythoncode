for row in range(1,5):
    for col in range(1,8):
        if(row==4) or (col+row==5) or (col-row==3):
            print("*",end="")
        else:
            print(end=" ")
    print()


for row in range(1,5):
    for col in range(1,8):
        if(row==1) or (row==col) or (row+col==8):
            print("*",end="")
        else:
            print(end=" ")
    print()
      