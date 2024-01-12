class animal:
def _init_(self,name):
    self.name=name

    def speak(self):
        print("welcome to inheritance")

class dog(animal):
    def speak(self):
        