from re import *
txt="pycharmisanid"
s=0
# a=txt.split()
# for i in txt:
#     s=s+1
# print(s)
vowels=["a","e","i","o","u"]                                                                                                                    
# for c in txt:
#     if c in vowels:
#         s=s+1
# print(s)

for c in txt:
    if c not in vowels:
        s=s+1
print(s)

