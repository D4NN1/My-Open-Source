class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

Force_1 = Vector(x1, y1)
Force_2 = Vector(x2, y2)

resultant = Force_1 + Force_2
print("Resultant Vector:", resultant)


