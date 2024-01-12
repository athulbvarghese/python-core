class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def function(self,empid):
        self.empid=empid
    #def function(self):
        print("name of the person:",self.name,"\n","age of the person:",self.age,"employee id:",self.empid)
p=Employee("athul",23)

p.function(12)
