# Auther: John Blue
# Time: 2023/2
# Object: Inheritance



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

    # override
    def area(self, s):
        print(s, "is in the Rectangle class area: ", self._width * self._height)



if __name__ == '__main__':
    shp = Rectangle(3, 3, "tri")
    print("create object")
    shp.spell_name()
    shp.area("shp")
    print("address:", hex(id(shp)))
    
    print("")
    
    shp_ref = shp
    print("reference object")
    shp_ref.spell_name()
    shp_ref.area("shp_ref")
    print("address:", hex(id(shp_ref)))
    
    print("")
    
    #shp_cop = shp[:]
    # shallow copy
    copy.copy(shp)
    # deep copy
    shp_cop = copy.deepcopy(shp)
    print("pure copy object")
    shp_cop.spell_name()
    shp_cop.area("shp_cop")
    print("address:", hex(id(shp_cop)))
