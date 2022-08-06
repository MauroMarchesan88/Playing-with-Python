from math import sqrt

a = int(input("Insert a variable: "))
b = int(input("Insert b variable: "))
c = int(input("Insert c variable: "))

# x = (-b + sqrt((b**2)-(4*a*c)))/(2*a)

x = (-b + (b*b - 4*a*c)**0.5) / (2*a)

print(x)
print(-x)
