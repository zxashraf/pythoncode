# sen="joel is very good student in may batch"
# words=sen.split(" ")

# print(sen.startswith("joel"))

# bool=sen.startswith("joel")
# print(bool)


# if bool==True:
    # print("the sentence is starting with 'joel'")

# if words[0]=="joel":
        # print("the sentence is starting with 'joel'")


import re
sen="is a very good student in may batch"
x=re.search("^joel",sen)
y=re.search("^joel",sen)
en=re.search("joel$",sen)
print(en)
print(x)
print(y)