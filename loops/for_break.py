# Example 1
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Example 2
for num in range(10):
    if num == 5:
        break
    print(num)

# Example 3
items = ["apple", "banana", "pear"]
for item in items:
    if item == "banana":
        break
    print(item)

# Example 4
for x in range(20):
    if x > 6:
        break
    print(x)

# Example 5
total = 0
for n in range(1, 10):
    total += n
    if total > 20:
        break
    print(total)
