# Boolean Operators: and, or, not

a = True
b = False

print(a and b)
print(a or b)
print(not a)

# Using comparisons with operators
x = 10
y = 5

print(x > 3 and y > 3)
print(x > 20 or y > 3)
print(not (x == y))

# Combining multiple conditions
age = 22
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")

# OR example
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
