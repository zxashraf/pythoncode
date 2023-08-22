f=open("C:/Users/ashra/OneDrive/Desktop/Python_code/fileinputoutput/data.txt")
words=[]

for line in f:
    text=line.rstrip("\n").split(" ")
    for w in text:
        words.append(w)
print(words)



