from abc import ABC, abstractmethod
#exercise 1
class Rectangle:
    def __init__(self,length,width):
        self.l=length
        self.w=width
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(self.l+self.w)
r1=Rectangle(5,6)
r2=Rectangle(3,4)
print(r1.area(),r2.area())
print(r1.perimeter(),r2.perimeter())


#exercise 2
class shape(ABC):
    def __init__(self,color):
        self.color=color
    def show(self):
        print(self.color)
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,color,radius):
        shape.__init__(self,color)
        self.radius=radius
    def area(self):
        return 3.14*(self.radius)**2
class Rectange(shape):
    def __init__(self,color,length,width):
        shape.__init__(self,color)
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    
r1=Rectange("red",5,6)
c1=circle("green",3)
st="yellow"


r1.show()
c1.show()

print(r1.area())
print(c1.area())


