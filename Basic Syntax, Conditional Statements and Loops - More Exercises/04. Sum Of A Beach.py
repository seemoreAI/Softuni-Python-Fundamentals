input_str = input()
keywords = ["sand", "water", "fish", "sun"]
total_count = 0
str_low = input_str.lower()

for word in keywords:
    total_count += str_low.count(word)

print(total_count)
