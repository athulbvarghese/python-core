class animal:
    def speak(self):
        print("animal speaking")
class dog (animal): 
    def bark(self):
        print("dog barking") 
 class dogchild(dog):
    def eat (self):
        print("eating bread.....")


        d=dogchild
        d.bark()
        d.speak()
        d.eat()
