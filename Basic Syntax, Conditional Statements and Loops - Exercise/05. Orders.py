number_of_orders = int(input())

for _ in range(number_of_orders):
    price_of_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not 0.01 <= price_of_capsule <= 100.00 or \
        1 <= days <= 31 or \
        1 <= capsules_per_day <= 2000:
        price = price_of_capsule * days * capsules_per_day
        print(f"The price for the coffee is: ${price}")
    else:
        continue
