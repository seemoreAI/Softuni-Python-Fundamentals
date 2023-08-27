num = input()
new_num = num
max_digit = int(num[0])
max_j = 0

for i in range(len(num)):
    max_digit = int(new_num[0])
    max_j = 0
    for j in range(len(new_num)):
        if int(new_num[j]) > max_digit:
            max_digit = int(new_num[j])
            max_j = j
    print(max_digit, end="")
    new_num = new_num[0:max_j] + new_num[max_j + 1:]
