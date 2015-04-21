# find the sum of all numbers divisable by 3 and 5 under 1000

sumNum = 0
i = 0

for i in range(0, 1000):
    if(i % 3):
        if(i % 5):
            print(str(i) + " is divisable by 3 and 5.\n")
            sumNum += i

print("Sum: " + str(sumNum))

            
