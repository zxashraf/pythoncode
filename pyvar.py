from re import *
rule="[a-zA-Z_][a-zA-Z0-9]*"
var_name="num#"

matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid")
else:
    print("valid")