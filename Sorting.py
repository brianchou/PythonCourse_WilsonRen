l = []
ll = []

maxScore = int(input("Please enter the max score :\t"))

for i in range(maxScore+1):
    l.append(0)

totalNumber = int(input("Please enter the total numbers :\t"))

for i in range(0, totalNumber):
    inputNumber = int(input("Please enter the number :\t"))
    l[inputNumber] += 1

for i in range(maxScore, -1, -1):
    for j in range(0, l[i]):
        ll.append(i)

print(ll)

