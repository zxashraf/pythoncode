data={
    "django":"framework",
    "react":"library"
    "fastapi":"framework",
    "Vue":"framework"
    "ajax":"library"
}
 


# wc={}
# for values in data.values():
#     if values in wc:
#         wc[values]+=1
#     else:
#         wc[values]=1
# print(wc)

wc={}
for k,v in data.items():
    if v in wc:
        wc[v].append(k)
    else:
        wc[v]=[k]
print(wc)

 


