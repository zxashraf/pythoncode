text="one 100 and 5"


words=(text.split(" "))

for w in words:
    if w.isdigit():
        print(w)

# list comprehension

words=[w for w in text.split(" ") if w.isdigit()]