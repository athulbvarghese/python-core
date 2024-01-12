class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def function(self):
        print("the barnd is",self.brand,"\n","model is:",self.model)
class Motorcycle(Vehicle):
    def function(self):
        print("the barnd is",self.brand,"\n","model is:",self.model)
p=Car("lamborgini","urus")
p.function()
d=Motorcycle("triumph","bobber")
d.function()
