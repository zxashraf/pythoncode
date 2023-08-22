fread=open("C:/Users/ashra/OneDrive/Desktop/Python_code/range_numbers/data.txt","r")
fwrite=open("C:/Users/ashra/OneDrive/Desktop/Python_code/range_numbers/leap.txt","w")

for line in fread:
    year=int(line.rstrip("\n"))
    if(year%400==0 and year%100==0):
        fwrite.write(str(year)+"\n")
    elif(year%100!=0 and year%4==0):
        fwrite.write(str(year)+"\n")
    