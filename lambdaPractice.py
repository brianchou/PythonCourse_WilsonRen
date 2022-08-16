list  = [1, 2, 3, 4]
list1 = []
list2 = []

func = [lambda x: x*x, lambda x: x+3]
funcCount = len(func)
listCount = len(list)

for i in range(funcCount):
    for j in range(listCount):
        a = func[i](list[j])
        list1.append(a)
        b = func[i](list1[j])
        list2.append(b)

print(list2[-listCount:])



