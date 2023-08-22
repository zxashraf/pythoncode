lst=[2,3,4,5,6]

sum=8
low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if(cur_sum==sum):
        print("pairs",lst[low],lst[upp])
        low+=1
    elif(cur_sum<sum):
        low+=1
    elif(cur_sum>sum):
        upp-=1