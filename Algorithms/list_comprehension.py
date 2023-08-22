lst=[3,4,5,6,7]


odds=[num   for num in lst if num%2!=0]
print(odds)

evens=[num for num in lst if num%2==0]
print(evens)


num_gt_five=[ num for num in lst if num>5]
print(num_gt_five)

cubes=[num**3 for num in lst ]
print(cubes)


