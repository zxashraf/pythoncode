class Users:
    data=[
        {"id":1,"username":"jhon","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
    ]
    def get(self):
        return self.data
    def retreive(self,id):
       return [u for u in self.data if u.get("id")==id]
    def post(self,obj):
        self.data.append(obj)
    def destroy(self,id):
        obj=[u for u in self.data if u.get("id")==id][0]
        self.data.remove(obj)
obj=Users()
student_data={"id":7,"username":"ram","email":"ram@gmail.com","password":"password@123"}
obj.post(student_data)
obj.destroy(5)
print(obj.get())
# print(obj.retreive(2))
# obj=Users()
# print(obj.getall_users())


# get()
# retreive(id)
# post()
# put(id)
# destroy(id)