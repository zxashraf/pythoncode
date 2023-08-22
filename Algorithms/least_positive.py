# lst=[1,3,4,6]
# find least positive missing integer from the given list
# p2-p1 => missing values

# lst=[1,3,4,8,9]
# for i in range(0,len(lst)):
    # element1=lst[i]
    # element2=lst[i+1]

    # if element1-element2 !=1:
        # print(element1+1,"is missing number")
        # break

lst=[1,2,4,5,8]
for i in range(0,len(lst)):
    if lst[0]!=1:
        print(1,"is missing")
        break
    else:
        elemt1=lst[i]
        elemt2=lst[i+1]
        if elemt2-elemt1 !=1:
            print(elemt1+1,"is missing")
            break

# lst=[2,3,4,4,5,5,6,7]
# find duplicate element from list