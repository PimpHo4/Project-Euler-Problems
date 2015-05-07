# project euler problem 3
div = 2

number = int(input("please enter a number: "))


while(number != 0):
    if (number % div != 0):
        div += 1
    else:
        number /= div
        print("Prime Factor: " + str(div) + "\n")
        if (number == 1):
            break

input('press any key to continue..')

