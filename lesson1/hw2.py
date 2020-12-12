
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

print(f"You've entered: a={a} , b={b}, c={c}")

d = b**2 - 4*a*c
print(f"D={d}")

x1 = (-b + d**0.5) / (2*a)
x2 = (-b - d**0.5) / (2*a)

print(f"x1={x1}, x2={x2}")
