f1=open("C:\\Users\\ashra\\OneDrive\\Desktop\\Python_code\\attendence\\data.txt")
f2=open("C:\\Users\\ashra\\OneDrive\\Desktop\\Python_code\\attendence\\present.txt")
total_students=set()
present=set()
for line in f1:
    total_students.add(line.rstrip("\n"))
print(total_students)

for line in f2:
    present.add(line.rstrip("\n"))
print(present)

absent_students=total_students-present
print(absent_students)
