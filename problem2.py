# Problem 2
# Project Euler
total = 0
one = 1
two = 2
three = 0

print("two: " + str(one) + "\n")
print("three: " + str(one) + "\n")

while(two <= 4000000):
    three = one + two
    if(two % 2 == 0):
        total += two

    one = two
    two = three
    print("two: " + str(two) + "\n")
    print("three: " + str(three) + "\n")


print("Sum: " + str(total) + "\n")


