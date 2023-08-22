# list=[2,3,5]
# list.append(6)
# print(list)


# # insert- to add a particular position in a list

# list.insert(0,1)
# print(list)


#creating empty list

emplist=[]
print(emplist)

#get element from the user snd each element of the list from the user,then add to list

length=int(input("enter the size of list: "))
for i in range(length):
    num=int(input(f" enter {i} th position element: "))
    emplist.append(num)
print(emplist)    