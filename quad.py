
import math
a = int(input("Enter the A coefficient: "))
b = int(input("Enter the B coefficient: "))
c = int(input("Enter the C coefficient: "))
x=int(input("What is x equal to?"))

print("The following Quadratic was entered", a,'X^2',b,'X+',c)
result = (a*x*x +b*x + x)
print("The value of the Quadratic is",result)

d = b**2-4*a*c # discriminant

if d < 0:
    print ("This equation has no real solution")
elif d == 0:
    x = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    print ("This equation has one solutions: ", x)
else:
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    x2 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    print ("This equation has two solutions: ", x1, " and", x2)