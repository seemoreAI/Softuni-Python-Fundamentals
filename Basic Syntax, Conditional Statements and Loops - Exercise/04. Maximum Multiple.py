divisor = int(input())
boundry = int(input())

for num in range(boundry,divisor-1,-1):
    if num % divisor == 0:
        print(num)
        break
