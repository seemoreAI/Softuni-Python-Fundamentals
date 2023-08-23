numb = float(input())
if 0 < abs(numb) < 1:
    print("small", end=" ")
elif abs(numb) > 1_000_000:
    print("large", end=" ")

if numb == 0:
    print("zero")
elif numb > 0:
    print("positive")
elif numb < 0:
    print("negative")
