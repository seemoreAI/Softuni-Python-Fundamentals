quantity_of_decorations = int(input())
days_left = int(input())
spirit = 0
cost = 0

for day in range(1,days_left+1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        spirit += 5
        cost += 2*quantity_of_decorations
    if day % 3 == 0:
        spirit += 13
        cost += 8*quantity_of_decorations
    if day % 5 == 0:
        spirit += 17
        cost += 15*quantity_of_decorations
    if day % 5 == 0 and day % 3 == 0:
        spirit += 30
    if day % 10 == 0:
        spirit -= 20
        cost += 23
if days_left % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")

