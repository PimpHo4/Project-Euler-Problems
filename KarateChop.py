#Karate Chop program

aList = [9, 8, 7, 5, 4, 3, 2, 10, 1, 6]


def bigChop():
    a = 5
    i = 0
    global i
    for number in aList:
        if (number > a):
            print("Good! number = " + str(number) + "\n")
            number = number / 2
            if (number == 3):
                print("Got it!")
                break
        else:
            print("That's not it! \n")

    i = i + 1
        



bigChop()
