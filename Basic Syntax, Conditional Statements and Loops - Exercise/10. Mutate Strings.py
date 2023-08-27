str_one = input()
str_two = input()

if len(str_one) == len(str_two):
    for i in range(1,len(str_one)+1):
        if str_one[i-1] != str_two[i-1]:
            print(str_two[0:i] + str_one[i:len(str_two)])
