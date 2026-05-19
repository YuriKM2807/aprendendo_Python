def twoSortedList(listA, listB):
    
    listFinal = []
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            listFinal.append(listA[a])
            a += 1
        else:
            listFinal.append(listB[b])
            b += 1

    listFinal += listA[a:]
    listFinal += listB[b:]
    print(listFinal)


list1 = [1, 1, 2, 4, 7, 10]
list2 = [1, 3, 4, 5]
twoSortedList(list1, list2)