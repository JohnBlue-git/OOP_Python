# Auther: John Blue
# Time: 2023/2
# Object: Encapsulation



import copy

# https://www.w3schools.com/python/python_inheritance.asp

class Shape:
    def __init__(self, a = 0, b = 0, s = "NULL"):
        self._width = a
        self._height = b
        self.__name = s
    
    def spell_name(self):
        print("the name: ", self.__name)
    def area(self, s):
        print(s, "is in the base class area: ", 0)

class Rectangle(Shape):
    def __init__(self, a = 0, b = 0, s = "NULL"):
        Shape.__init__(self, a, b, s)

    def area(self, s):
        print(s, "is in the Rectangle class area: ", self._width * self._height)

class Triangle(Shape):
    def __init__(self, a = 0, b = 0, s = "NULL"):
        Shape.__init__(self, a, b, s)

    def area(self, s):
        print(s, "is in the Triangle class area: ", self._width * self._height / 2)

class Circle(Shape):
    def __init__(self, a = 0, b = 0, s = "NULL"):
        Shape.__init__(self, a, b, s)

    def area(self, s):
        print(s, "is in the Circle class area: ", self._width * self._height * 3.14)


if __name__ == '__main__':
    rec = Rectangle(3, 3, "rec")
    rec.spell_name()
    rec.area("rec")
    
    print("")
    
    tri = Triangle(3, 3, "tri")
    tri.spell_name()
    tri.area("tri")
    
    print("")
    
    cir = Circle(3, 3, "cir")
    cir.spell_name()
    cir.area("shp")
    
    print("")
    
    Set = [Rectangle(3, 3, "rec"), Triangle(3, 3, "tri"), Circle(3, 3, "cir")]
    for s in Set:
        s.area("s")
