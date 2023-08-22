import  datetime
class Operations:
    n1:int
    n2:int

    def __init__ (self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1+self.n2
    def product(self):
        return self.n1*self.n2
    @staticmethod
    def getdate():
        return datetime.date.today()
op=Operations(100,200)
print(op.add())
print(op.product())
print(Operations.getdate())