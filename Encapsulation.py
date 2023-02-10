# Auther: John Blue
# Time: 2023/2
# Object: display how to use continue and break



import copy

# const is possible in python, but difficult to construct one

class Shape:
    # private
    #self.__name
    # protected
    #self._width
    #self._height
    # public
    # constructor
    def __init__(self, a = 0, b = 0, s = "NULL"):
        self._width = a
        self._height = b
        self.__name = s
    # copy constructor
    #https://stackoverflow.com/questions/1241148/copy-constructor-in-python
    # deconstructor
    # (though it is not very neccessary to del object in python, python would collect garbage automatically)
    #def __del__(self):
        #print("Shape bye~")
        
    # operator
    # assignment
    # (not possible)
    # (https://stackoverflow.com/questions/11024646/is-it-possible-to-overload-python-assignment)
    # (other operator)
    # (https://www.geeksforgeeks.org/operator-overloading-in-python/)
    # address
    def __getitem__(self, n):
        if n == 0 :
            return self._width
        elif n == 1 :
          return self._height
        else :
          print("out of list")
          return - 1;
    
    # function
    def spell_name(self):
        print("the name: ", self.__name)
    def area(self, s):
        print(s, "is in the base class area: ", 0)

if __name__ == '__main__':
    shp = Shape(3, 3)
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
    
    # shallow copy (cannot copy function)
    shp_cop = shp[:]
    #
    shp_cop = copy.deepcopy(shp)
    print("pure copy object")
    shp_cop.spell_name()
    shp_cop.area("shp_cop")
    print("address:", hex(id(shp_cop)))
