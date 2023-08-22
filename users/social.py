f=open("C:/Users/ashra/OneDrive/Desktop/Python_code/users/data.txt","r")
users=[]

for line in f:
    text=line.rstrip("\n")
    name,followers,followings=text.split(",")
    print(name,followers,followings)