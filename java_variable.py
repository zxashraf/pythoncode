from re import *
rule="[a-zA-Z][a-zA-Z0-9$_]{0,10}"
var_name="num_two"
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")