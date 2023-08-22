weather=[
    {"tvm":25},
    {"apy":23},
    {"kty":27},
    {"idk":18},
    {"tsr":28},
    {"ekm":29},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
    {"tsr":22},
]
temp={}
for t in weather:
    for k,v in t.items():
        district_name=k
        current_temp=v
        if district_name in temp:
            old_temp=temp[district_name]
            if current_temp>old_temp:
                temp[district_name]=current_temp
        else:
            temp[district_name]=current_temp
print(max(temp,key=lambda k:temp.get(k)))




