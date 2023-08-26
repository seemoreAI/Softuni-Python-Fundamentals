number_of_orders = int(input())
total_price = 0
for _ in range(number_of_orders):
    price_of_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_of_capsule <= 100.00 and \
            1 <= days <= 31 and \
            1 <= capsules_per_day <= 2000:
        price = price_of_capsule * days * capsules_per_day
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")
    else:
        continue
print(f"Total: ${total_price:.2f}")
