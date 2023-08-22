stud_name=[]
length=int(input("enter the size of the list: "))
for i in range(length):
    name=input(f"enter{i}th name: ")
    stud_name.append(name)
ch_name=input("enter a name: ")

for s in range(length):
    if(stud_name==ch_name):
        stud_name[s]="Anamika"
        break
    elif(s==length-1):
        stud_name[0]="Amal"
print(stud_name)

#if duplicate values are present how the values will be changed if  match found or note
#i/p=> [a,b,c,a] =>ch_name=a, o/p=>[Anamika,b,c,Anamika]


stud_name=["a","b","c","a"]
flag=0
ch_name=input("enter a name: ")
 
for i in range(len(stud_name)):
    if(ch_name==stud_name[i]):
        stud_name[i]="Anamika"
        flag=1
if(flag==0):
    stud_name.insert(1,"Amal")
print(stud_name)