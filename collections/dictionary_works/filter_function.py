lst=[1,2,3,4,5]

# print all numbers >3

num_gt3=list(filter(lambda n:n>3,lst))
print(num_gt3)

# print odd numbers

odds=list(filter(lambda n:n%2!=0,lst))
print(odds)

# print even number

even=list(filter(lambda n:n%2==0,lst))
print(even)