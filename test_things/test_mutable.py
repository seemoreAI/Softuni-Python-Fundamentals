x = ["apple", "banana"]
z = x
print(z)
print(x)
print(z is x)

x.append("grapes")

print(z)
print(x)
print(z is x)
