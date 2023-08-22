# from json import load
# f=open("C:/Users/ashra/OneDrive/Desktop/Python_code/jsonprocess/data.json","r")
# data=load(f)
# print(data)
# f.close()
from json import load
with open("C:/Users/ashra/OneDrive/Desktop/Python_code/jsonprocess/data.json","r") as f:
    data=load(f)

for u in data:
    print(u.get("name"))