class Vehicle:
  
  def __init__(self,make,model):
    self.make=make
    self.model=model

  def start(self):
    print(self.model,"Started")

  def stop(self):
    print(self.model,"Stopped")

class Car(Vehicle):
  
  def display(self,num):
    self.num=num
    print("Make year of car:",self.make,"\n","Model of car:",self.model,"\n","Number of doors of car:",self.num)

class Motorcycle(Vehicle):
 
  def display(self,num):
    self.num=num
    print("Make year of motorcycle:",self.make,"\n","Model of motorcycle:",self.model,"\n","Number of wheels of motorcycle:",self.num)


c=Car(2010,"polo")
c.start()
c.display(4)
c.stop()

print("________________________")

m=Motorcycle(2018,"twin street")
m.start()
m.display(2)
m.stop()
