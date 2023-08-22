num=13 
is_prime=True
for i in range(1,num):
    if(num%2==0):
        is_prime=False
        break
if(is_prime==True):
    print(num,"is prime")
else:
    print(num,"is not prime")