# Example 1
i = 1
while True:
    if i == 4:
        break
    print(i)
    i += 1

# Example 2
x = 0
while x < 10:
    if x == 6:
        break
    print(x)
    x += 1

# Example 3
num = 5
while num > 0:
    if num == 2:
        break
    print(num)
    num -= 1

# Example 4
while True:
    user = input("Enter number: ")
    if user == "0":
        break
    print("You entered:", user)

# Example 5
total = 0
while True:
    total += 3
    if total > 15:
        break
    print(total)
