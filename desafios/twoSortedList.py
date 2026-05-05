listA = [1, 2, 4]
listB = [1, 3, 4]
listFinal = []
a = 0
b = 0
while a < len(listA) or b < len(listB):
    while a < b:
        listFinal.append(listA[a])
        a += 1
    while b < a:
        listFinal.append(listB[b])
        b += 1
        
print(listFinal)