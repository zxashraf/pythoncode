f=open("C:/Users/ashra/OneDrive/Desktop/Python_code/leap_year/data.txt","w")
years=[2000,2024,1991,1995,1200,1400,1234]
for year in years:
    if(year%100==0 and year%400==0):
        print(year)
    elif(year%100!=0 and year%4==0):
        f.write(str(year)+"\n")


