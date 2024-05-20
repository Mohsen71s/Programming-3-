
"""
   Singleton Method is a type of Creational Design pattern that makes sure that only one instance 
   of a class exists. such as db connection
"""
import copy

class Singleton:
    def __new__(cls) :
        return cls
    
print(f"id(Singleton)\t= {id(Singleton)}")
OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")