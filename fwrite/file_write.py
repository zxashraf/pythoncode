f=open("C:/Users/ashra/OneDrive/Desktop/Python_code/fwrite/data.txt","w")

languages=[
    "python","java","c","c++"
]

for l in languages:
    f.write(l+"\n")
print("finished")