num=153
num2=num
cnt=len(str(num))
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit**cnt
    num=num//10
print(sum)
if(num2==sum):
    print("Armstrong number")
else:
    print("Not armstrong number")
  