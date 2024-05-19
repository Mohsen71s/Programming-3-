"""
Facade is a type of Structural Design Patterns
"""

"""Facade pattern with an example of WashingMachine"""
"""
Facade is a type of Structural Design Patterns
"""

"""Facade pattern with an example of WashingMachine"""

class Washing: 
    def wash(self):
        print("Washing")

class Rinsing:
    def Rinse(self):
        print("Rinsing")

class Spinning:
    def Spinne(self):
        print("Spinning")
    
class WashingMachine:
    def __init__(self):
        self.washing=Washing()
        self.Rinsing=Rinsing()
        self.Spinning=Spinning()
    def startWashing(self):
        self.washing.wash()
        self.Rinsing.Rinse()
        self.Spinning.Spinne()

if __name__ == "__main__": 

	washingMachine = WashingMachine() 
	washingMachine.startWashing() 
