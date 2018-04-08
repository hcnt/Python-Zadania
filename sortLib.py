def wstaw_ros(lista, element, pocz, kon):
    for i in range(pocz,kon+1):
        if element > lista[i]:
            lista.insert(i,element)
            return lista
    


lista = [1,7,9,1,10]
print(wstaw_ros(lista, 3, 0,0))



def sort_ros_wst(t):
    posortowane_elementy = 0
    for i in range(len(t)-1):
        wstaw_ros(t,t[len(t)-1],0,i)
        t.pop()
        print(t)
    return t



t = [1,5,3,6,4]
#print(t)
#print(sort_ros_wst(t))

