text="ABABC"

# find first recursive charecter

wc={}
count=0
for ch in text:
    if(ch in wc):
        print(ch,"is first recursive charector")
        break
    else:
        wc[ch]=1

#  To check count of charector

wc={}
for ch in text:
    if(ch in wc):
        wc[ch]+=1
        
    else:
        wc[ch]=1
print(wc)


# word count
words=["hwllo","good","aabbccdef","morning"]
out=sorted(words,reverse=False,key=lambda w:len(w))
print(out)


text="ABBAACDA"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(min(wc,key=lambda k:wc.get(k)))

