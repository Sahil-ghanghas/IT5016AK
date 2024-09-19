"""
Author= Sahil
"""
# Class Person
class person():
     def __init__(self,name,age):
        self.name=name
        self.age=age
     def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} year old.")
Person1= person ("Charanpreet", 20)
Person1.greet()        

