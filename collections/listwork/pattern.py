arr=[2,3,4]
op=[]
# find total sum of array

total_arr=sum(arr)
# print(total_arr)

# sub each element with total

# for num in arr:
#     print(total_arr-num)

for i in arr:
    res=total_arr-i
    op.append(res)
print(op)
