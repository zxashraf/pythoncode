lst=[[1,2],[4,50],[50,45]]


# print all numbers

for sublist in lst:
    for num in sublist:
        print(num)

# print all numbers > 5

for sublist in lst:
    for num in sublist:
        if (num>5):
            print(num)

# list comprehension

allnumbers=[num for sublist in lst for num in sublist]
print(allnumbers)

number_gt_5=[num for sublist in lst for num in sublist if (num>5)]
print(number_gt_5)
