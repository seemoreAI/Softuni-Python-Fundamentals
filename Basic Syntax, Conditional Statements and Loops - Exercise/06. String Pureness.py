n = int(input())

for _ in range(n):
    my_str = input()
    for i in range(len(my_str)):
        if my_str[i] in (",._"):
            print(f"{my_str} is not pure!")
            break
    else:
        print(f"{my_str} is pure.")


# shorter way to to it :
#
# n = int(input())
#
# for _ in range(n):
#     my_str = input()
#     if any(char in ",._" for char in my_str):
#         print(f"{my_str} is not pure!")
#     else:
#         print(f"{my_str} is pure.")
