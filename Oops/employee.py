class Employee:
    id:int
    name:str
    desig:str
    salary:int

    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary
    
    def get_emp(self):
        print(self.id,self.name,self.desig,self.salary)

emp1=Employee(1000,"rocky","hr",34000)
emp1.get_emp()