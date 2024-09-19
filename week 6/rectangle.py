"""
Author= sahil
"""
# class rectangle
class Rectangle():
    def __init__(self,width,height):
         self.width=width
         self.height=height
    def area(self):
         return self.width*self.height
    def perimeter(self):
         return 2*(self.width+self.height)
rect=Rectangle(4,6)
print(F"Area of the rectangle is: {rect.area()}")
print(F"Perimeter of rectangle is:{rect.perimeter()}")    



