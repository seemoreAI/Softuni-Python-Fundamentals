
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

for i in range(len(thislist)):
    print(thislist[i])

[print(x) for x in thislist]

newlist = [x for x in thislist if "a" in x]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in thislist]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(100,200) if x % 7 == 0]
print(newlist)