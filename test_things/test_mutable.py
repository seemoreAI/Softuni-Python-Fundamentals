x = ["abc", 34, True, 40, "male"]
z = x
print(z)
print(x)
print(z is x)

x.append("grapes")

print(z)
print(x)
print(z is x)

print(len(x))

print(type(x))