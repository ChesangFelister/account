class Circle:
    def __init__(self,radius):
        self.radius = radius
    def circle_area(self):
        radius = self.radius
        A = (22/7)*(radius*radius)
        print(A)
    def circumference(self):
    	radius=self.radius
    	C=2*(22/7)*radius
    	print(C)

class Square:
	def __init__ (self,side):
		self.side=side

	def area_square(self):
		side=self.side
		A=side*side
		print(A)
	def perimeter(self):
		side=self.side
		P=4*side
		print(P)

class Rectangle:
	def __init__(self,length,width):
		self.length=length
		self.width=width

	def Area_Rectangle(self):
		length=self.length
		width=self.width
		A=length*width
		print(A)

	def perimeter(self):
		length=self.length
		width=self.width
		p=2*(length+width)
		print(p)

class Sphere:
	def __init__(self,radius):
		self.radius=radius

	def Area_sphere(self):
		radius=self.radius
		A=4*(22/7)*(radius*radius)
		print(A)

	def volume(self):
		radius=self.radius
		V=4/3*(22/7)*(radius*radius*radius)
		print(V)




				