# lst1=[10,14,15,20,21]
# lst2=[8,9,20,21,22]

# for n1 in lst1:
#     for n2 in lst2:
#         if(n1==n2):
#             print(n1)

# element=20
# lst=[1,2,3,4]
# create a program to search from list
# element found or element not found


lst1=[8,14,15,20,21]
lst2=[9,10,20,21,22]
(p1,p2)=(0,0)
while(p1<len(lst1) and p2<len(lst2)):
    if(lst1[p1]==lst2[p2]):
        print(lst1[p1])
        p1+=1
    elif(lst1[p1]<lst2[p2]):
        p1+=1
    elif(lst1[p1]>lst2[p2]):
        p2+=1






