def f(m):
    if m <=1:
        return 1
    else:
        for i in range(0,m):
            return f(m-1)+f(m-2)
        




print(f(-10))#1 
print(f(0))#1
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))
