import math
class Circle :
  def __init__(self, radius):
    self.radius=radius
    

  def get_diameter(self):
        return self.radius * 2

  def get_area(self):
        return math.pi * (self.radius ** 2)

  def __str__(self):
        return f"Circle with radius: {self.radius}"

  def __add__(self, other):
        return Circle(self.radius + other.radius)

  def __lt__(self, other):
        return self.radius < other.radius

  def __eq__(self, other):
        return self.radius == other.radius

c1 = Circle(3)
c2 = Circle(5)

print(c1) 
print("Diameter:", c1.get_diameter())  
print("Area:", c1.get_area()) 
c3 = c1 + c2
print("New circle from addition:", c3)  

print("Is c1 smaller than c2?", c1 < c2)  
print("Are c1 and c2 equal?", c1 == c2)   

circle_list = [c2, c1, c3]
circle_list.sort()
for c in circle_list:
    print(c)

