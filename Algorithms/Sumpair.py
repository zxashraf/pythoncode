lst=[2,3,4,5]

# sum=8
# for i in lst:
#     for j in lst:
#         if(i!=j and i<j):
#             cur_sum=i+j
#             if(cur_sum==sum):
#                 print(i,j)



low=0
sum=8
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if(cur_sum==sum):
        print("pairs",lst[low],lst[upp])
        break
    elif(cur_sum<sum):
        low+=1
    elif(cur_sum>sum):
        upp-=1
   