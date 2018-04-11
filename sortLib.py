def swap(tab,x,y):
    a = tab[y]
    tab[y] = tab[x]
    tab[x] = a
    return tab

def indexOfMinimum(tab,start,end):
    min = tab[start]
    minIndex = start
    for i in range(start+1,end+1):
        if tab[i] < min:
            min = tab[i]
            minIndex = i
    return minIndex

def bubbleSort(tab):
    for i in range(len(tab),0,-1):
        for j in range(0,i):
            if(j < len(tab)-1 and tab[j] >= tab[j+1]):
                tab = swap(tab,j,j+1)

    return tab

def insertionSort(tab):
    for i in range(1,len(tab)):
        x = indexOfMinimum(tab,i,len(tab)-1)
        while tab[x] < tab[x-1] and x>0:
            tab = swap(tab,x,x-1)
            x-=1
    return tab

def selectionSort(tab):
    for i in range(0,len(tab)):
        min = indexOfMinimum(tab,i,len(tab)-1)
        tab = swap(tab,i,min)
    return tab


def quickSort(tab):
    pivot = tab[0]
    tab.pop(0)
    smaller = []
    bigger = []
    for i in range(0,len(tab)):
        if tab[i] < pivot:
            smaller.append(tab[i])
        else:
            bigger.append(tab[i])

    if(len(smaller) > 1):
        smaller = quickSort(smaller)
    if(len(bigger) > 1):
        bigger = quickSort(bigger)

    p = []
    p.append(pivot)

    return smaller + p + bigger

def quickSortInPlace(tab):
    def aux(tab,start,end):
        pivot = tab[start]
        for i in range(start,end):
            if(tab[i]< pivot):
                tab.insert(start,tab[i])
                tab.pop(i+1)
        pivotIndex = tab.index(pivot)

        if(pivotIndex > start + 1):
            tab = aux(tab,start,pivotIndex)
        if(pivotIndex < end - 2):
            tab = aux(tab,pivotIndex+1,end)

        return tab

    return(aux(tab,0,len(tab)))



t3 = [20,-321,12,32,12,13,44,5,432,2135]
t2 = [43,43,321,54,13,44,5,1,2135]
t = [6,3,1,7,5]
# print(insertionSort(t3))
# print(bubbleSort(t3))
# print(selectionSort(t3))
# print(quickSort(t3))
print(quickSortInPlace(t3))
