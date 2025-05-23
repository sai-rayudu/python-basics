#class and object
class a1:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def get_details(self):
        print(f"Name:{self.name},age:{self.age},id:{self.id}")


obj=a1("sai","23","7347534")
obj.get_details()

class parent:
    def __init__(self,name):
        self.name=name
    def sd(self):
        print(f"parentName:{self.name}")

class child(parent):
    def __init__(self,name):
        super().__init__(name)

obj1=child("ranga")
print(obj1.name)
obj1.sd()

