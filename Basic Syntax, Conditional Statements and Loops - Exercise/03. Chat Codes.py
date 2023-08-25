messages_number = int(input())
for _ in range(messages_number):
    msg1 = int(input())
    if msg1 == 88:
        print("Hello")
    elif msg1 == 86:
        print("How are you?")
    elif msg1 < 88:
        print("GREAT!")
    else:
        print("Bye.")
