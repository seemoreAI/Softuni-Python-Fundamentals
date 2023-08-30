my_str = input()
my_list = my_str.split(', ')
numb = 0

if my_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for animal in reversed(list(my_list)):
        numb += 1
        if animal == "wolf":
            print(f"Oi! Sheep number {numb-1}! You are about to be eaten by a wolf!")
            break
