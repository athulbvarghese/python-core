class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area(self,radius):
        self.radius=radius
        print("radius=",3.14*self.radius**2)
class Rectangle(Shape):
    def area(self,length,height):
        self.length=length
        self.height=height
        print("area of rectangle=",self.length*self.height)
a=Circle()
a.area(5)
b=Rectangle()
b.area(4,5)

