# create a list of 5 birds , print all the elements one by one , change 3rd bird to "penguine"

# Birds=["parrot","crow","eagle","pigeon","hen"]
Birds=["parrot","crow","duck","pigeon","hen"]
print(Birds[0])
print(Birds[1])
print(Birds[2])
print(Birds[3])
print(Birds[4])


# Birds[2]="penguine"
# print(Birds)
# Birds[4]="peacock"
# print(Birds)
if(Birds[2]=="penguine"):
    Birds[2]="iam penguine"
else:
    Birds[2]="iam not penguine"
print(Birds)