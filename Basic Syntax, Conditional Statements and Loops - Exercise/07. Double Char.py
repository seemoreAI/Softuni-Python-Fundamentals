while True:
    input_string = input()
    if input_string == "End":
        break
    if input_string == "SoftUni":
        continue
    for i in range(len(input_string)):
        print(input_string[i]*2,end="")
    print()
