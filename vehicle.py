# kl 19 H 1
from re import *
# rule="[K][L][-][0-9]{2}[-][A-Z]{1,2}[-][0-9]{4}"
# number="KL-19-H-0001"
# matcher=fullmatch(rule,number)
# if matcher==None:
#     print("invalid")
# else:
#     print("valid")

# All india

rule="[K-L]{2}[-][0-9]{2}[-][A-Z]{1,2}[-][0-9]{4}"
number="MH-01-A-4444"
matcher=fullmatch(rule,number)
if matcher==None:
    print("invalid")
else:
    print("valid")