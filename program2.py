text="england promised to continue its aggressive to test cricket"
# print the words to start with vowels

vowels={"a","e","i","o","u"}

words=text.split()

for w in words:
    if w[0].casefold() in vowels:
        print(w)

# list comprehension

words=[w for w in text.split(" ") if w[0].casefold() in vowels]
