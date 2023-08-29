#Write a program that takes a single string and
#prints a list of all the capital letters indices.
# print([index for index, char in enumerate(input()) if char.isupper()])
my_list = []
for index, char in enumerate(input()):
    if char.isupper():
        my_list.append(index)
print(my_list)
