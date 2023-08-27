coffee = 0
while coffee <= 5:
    command = input()
    if command == "END":
        print(coffee)
        break
    elif command == "coding" or \
            command == "dog" or \
            command == "cat" or \
            command == "movie":
        coffee += 1
    elif command == "CODING" or \
            command == "DOG" or \
            command == "MOVIE" or \
            command == "CAT":
        coffee += 2
else:
    print("You need extra sleep")
