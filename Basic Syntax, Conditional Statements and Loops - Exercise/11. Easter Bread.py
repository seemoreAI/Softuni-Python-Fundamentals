budget = float(input())
flower_price = float(input())
eggs_price = flower_price*0.75
milk_price = flower_price*1.25
eggs = 0

loaves = int(budget // (flower_price + eggs_price + milk_price/4))
budget = f"{budget % (flower_price + eggs_price + milk_price/4):.2f}"

for current_loaf in range(1,loaves+1):
    eggs += 3
    if current_loaf %3 == 0:
        eggs -= current_loaf - 2




print(f"You made {loaves} loaves of Easter bread! Now you have {eggs} eggs and {budget}BGN left.")




