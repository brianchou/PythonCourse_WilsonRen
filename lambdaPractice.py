func = [lambda x: x*x, lambda x: x+3, lambda x: x+5, lambda x: x+10, lambda x: x+20]
listX = [1, 2, 3, 4]

funcCount = len(func)
listCount = len(listX)

listY = []

listY.append(list(map(func[0], listX)))

for i in range(1, funcCount):
    for j in range(listCount):
        listY.append(list(map(func[i], listY[j])))
        if i < (funcCount-1):
            i += 1
print(listY[funcCount-1])







